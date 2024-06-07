# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

import os, json
from azure.cli.testsdk import ScenarioTest
from azure.cli.testsdk import ResourceGroupPreparer
from .example_steps import step_private_link_resource_list
from .example_steps import step_private_link_scope_create
from .example_steps import step_private_link_scope_update
from .example_steps import step_private_link_scope_show
from .example_steps import step_private_link_scope_list
from .example_steps import step_private_link_scope_list2
from .example_steps import step_private_link_scope_update_tag
from .example_steps import step_private_endpoint_connection_update
from .example_steps import step_private_endpoint_connection_list
from .example_steps import step_private_endpoint_connection_show
from .example_steps import step_private_endpoint_connection_delete
from .example_steps import step_private_link_scope_delete
from .. import (
    try_manual,
    raise_if,
    calc_coverage
)
from azure.cli.testsdk.scenario_tests import (
    live_only
)

TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


class RunCommandScenarioTest(ScenarioTest):
    @live_only()
    @ResourceGroupPreparer(name_prefix='cli_test_runcommand')
    def test_run_command(self):
        rand_string = 'test'
        self.kwargs.update({
            'machine': 'testmachine',
            'rg': 'ytongtest',
            'location': 'centraluseuap',
            'subscription': '00000000-0000-0000-0000-000000000000',
            'runcommand': 'myRunCommand',
        })

        parameters_string = '''[{"name":"param1","value":"value1"}]'''
        self.kwargs['parameters'] = json.dumps(parameters_string)

        self.cmd('az connectedmachine run-command create '
                '--resource-group "{rg}" '
                '--location "{location}" '
                '--script "Write-Host Hello World!" '
                '--name "{runcommand}" '
                '--machine-name "{machine}" '
                '--parameters "{parameters}" '
                '--subscription "{subscription}"',
                checks=[
                    self.check('type','Microsoft.HybridCompute/machines/runcommands'),
                    self.check('instanceView.executionState','Succeeded')
                ])
        
        self.cmd('az connectedmachine run-command list '
                '--resource-group "{rg}" '
                '--machine-name "{machine}"',
                checks=[
                    self.check('length(@)', 1)
                ])

        self.cmd('az connectedmachine run-command show '
                '--resource-group "{rg}" '
                '--name "{runcommand}" '
                '--machine-name "{machine}"',
                checks=[
                    self.check('type','Microsoft.HybridCompute/machines/runcommands'),
                    self.check('instanceView.executionState','Succeeded')
                ])

        self.cmd('az connectedmachine run-command update '
                '--resource-group "{rg}" '
                '--name "{runcommand}" '
                '--machine-name "{machine}" '
                '--subscription "{subscription}" '
                '--tags Tag1="Value1"',
                checks=[
                    self.check('type','Microsoft.HybridCompute/machines/runcommands'),
                    self.check('instanceView.executionState','Succeeded')
                ])

        self.cmd('az connectedmachine run-command delete '
                '--resource-group "{rg}" '
                '--name "{runcommand}" '
                '--machine-name "{machine}" --yes',
                checks=[])
