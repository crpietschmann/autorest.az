# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines
# pylint: disable=too-many-statements

from knack.arguments import CLIArgumentType
from azure.cli.core.commands.parameters import (
    tags_type,
    get_enum_type,
    resource_group_name_type,
    get_location_type
)
from azure.cli.core.commands.validators import get_default_location_from_resource_group
from azext_datafactory.action import (
    AddFactoryVstsConfiguration,
    AddFactoryGitHubConfiguration,
    AddFakeIdentity
)


def load_arguments(self, _):

    with self.argument_context('datafactory list') as c:
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('datafactory show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', options_list=['--name', '-n'], help='The factory name.', id_part='name')
        c.argument('if_none_match', help='ETag of the factory entity. Should only be specified for get. If the ETag mat'
                   'ches the existing entity tag, or if * was provided, then no content will be returned.')

    with self.argument_context('datafactory create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', options_list=['--name', '-n'], help='The factory name.')
        c.argument('if_match', help='ETag of the factory entity. Should only be specified for update, for which it shou'
                   'ld match existing entity or can be * for unconditional update.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx),
                   validator=get_default_location_from_resource_group)
        c.argument('tags', tags_type)
        c.argument('factory_vsts_configuration', action=AddFactoryVstsConfiguration, nargs='+', help='Factory\'s VSTS r'
                   'epo information.', arg_group='RepoConfiguration')
        c.argument('factory_git_hub_configuration', action=AddFactoryGitHubConfiguration, nargs='+', help='Factory\'s G'
                   'itHub repo information.', arg_group='RepoConfiguration')
        c.argument('fake_identity', action=AddFakeIdentity, nargs='+', help='This is only for az test.')
        c.argument('zones', nargs='+', help='This is only for az test.')

    with self.argument_context('datafactory update') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', options_list=['--name', '-n'], help='The factory name.', id_part='name')
        c.argument('tags', tags_type)

    with self.argument_context('datafactory delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', options_list=['--name', '-n'], help='The factory name.', id_part='name')

    with self.argument_context('datafactory configure-factory-repo') as c:
        c.argument('location_id', help='The location identifier.', id_part='name')
        c.argument('factory_resource_id', help='The factory resource id.')
        c.argument('factory_vsts_configuration', action=AddFactoryVstsConfiguration, nargs='+', help='Factory\'s VSTS r'
                   'epo information.', arg_group='RepoConfiguration')
        c.argument('factory_git_hub_configuration', action=AddFactoryGitHubConfiguration, nargs='+', help='Factory\'s G'
                   'itHub repo information.', arg_group='RepoConfiguration')

    with self.argument_context('datafactory get-data-plane-access') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', options_list=['--name', '-n'], help='The factory name.', id_part='name')
        c.argument('permissions', help='The string with permissions for Data Plane access. Currently only \'r\' is supp'
                   'orted which grants read only access.')
        c.argument('access_resource_path', help='The resource path to get access relative to factory. Currently only em'
                   'pty string is supported which corresponds to the factory resource.')
        c.argument('profile_name', help='The name of the profile. Currently only the default is supported. The default '
                   'value is DefaultProfile.')
        c.argument('start_time', help='Start time for the token. If not specified the current time will be used.')
        c.argument('expire_time', help='Expiration time for the token. Maximum duration for the token is eight hours an'
                   'd by default the token will expire in eight hours.')

    with self.argument_context('datafactory get-git-hub-access-token') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', options_list=['--name', '-n'], help='The factory name.', id_part='name')
        c.argument('git_hub_access_code', help='GitHub access code.')
        c.argument('git_hub_client_id', help='GitHub application client ID.')
        c.argument('git_hub_access_token_base_url', help='GitHub access token base URL.')

    with self.argument_context('datafactory trigger list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', help='The factory name.')

    with self.argument_context('datafactory trigger show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', help='The factory name.', id_part='name')
        c.argument('trigger_name', options_list=['--name', '-n'], help='The trigger name.', id_part='child_name_1')
        c.argument('if_none_match', help='ETag of the trigger entity. Should only be specified for get. If the ETag mat'
                   'ches the existing entity tag, or if * was provided, then no content will be returned.')

    with self.argument_context('datafactory trigger create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', help='The factory name.')
        c.argument('trigger_name', options_list=['--name', '-n'], help='The trigger name.')
        c.argument('if_match', help='ETag of the trigger entity.  Should only be specified for update, for which it sho'
                   'uld match existing entity or can be * for unconditional update.')
        c.argument('properties', arg_type=CLIArgumentType(options_list=['--properties'], help='Properties of the trigge'
                   'r. Expected value: json-string/@json-file.'))

    with self.argument_context('datafactory trigger update') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', help='The factory name.', id_part='name')
        c.argument('trigger_name', options_list=['--name', '-n'], help='The trigger name.', id_part='child_name_1')
        c.argument('if_match', help='ETag of the trigger entity.  Should only be specified for update, for which it sho'
                   'uld match existing entity or can be * for unconditional update.')
        c.argument('properties', arg_type=CLIArgumentType(options_list=['--properties'], help='Properties of the trigge'
                   'r. Expected value: json-string/@json-file.'))

    with self.argument_context('datafactory trigger delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', help='The factory name.', id_part='name')
        c.argument('trigger_name', options_list=['--name', '-n'], help='The trigger name.', id_part='child_name_1')

    with self.argument_context('datafactory trigger get-event-subscription-status') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', help='The factory name.', id_part='name')
        c.argument('trigger_name', options_list=['--name', '-n'], help='The trigger name.', id_part='child_name_1')

    with self.argument_context('datafactory trigger query-by-factory') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', help='The factory name.', id_part='name')
        c.argument('continuation_token', help='The continuation token for getting the next page of results. Null for fi'
                   'rst page.')
        c.argument('parent_trigger_name', help='The name of the parent TumblingWindowTrigger to get the child rerun tri'
                   'ggers')

    with self.argument_context('datafactory trigger start') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', help='The factory name.', id_part='name')
        c.argument('trigger_name', options_list=['--name', '-n'], help='The trigger name.', id_part='child_name_1')

    with self.argument_context('datafactory trigger stop') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', help='The factory name.', id_part='name')
        c.argument('trigger_name', options_list=['--name', '-n'], help='The trigger name.', id_part='child_name_1')

    with self.argument_context('datafactory trigger subscribe-to-event') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', help='The factory name.', id_part='name')
        c.argument('trigger_name', options_list=['--name', '-n'], help='The trigger name.', id_part='child_name_1')

    with self.argument_context('datafactory trigger unsubscribe-from-event') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', help='The factory name.', id_part='name')
        c.argument('trigger_name', options_list=['--name', '-n'], help='The trigger name.', id_part='child_name_1')

    with self.argument_context('datafactory trigger wait') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', help='The factory name.', id_part='name')
        c.argument('trigger_name', options_list=['--name', '-n'], help='The trigger name.', id_part='child_name_1')
        c.argument('if_none_match', help='ETag of the trigger entity. Should only be specified for get. If the ETag mat'
                   'ches the existing entity tag, or if * was provided, then no content will be returned.')

    with self.argument_context('datafactory integration-runtime list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', help='The factory name.')

    with self.argument_context('datafactory integration-runtime show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', help='The factory name.', id_part='name')
        c.argument('integration_runtime_name', options_list=['--name', '-n'], help='The integration runtime name.',
                   id_part='child_name_1')
        c.argument('if_none_match', help='ETag of the integration runtime entity. Should only be specified for get. If '
                   'the ETag matches the existing entity tag, or if * was provided, then no content will be returned.')

    with self.argument_context('datafactory integration-runtime linked-integration-runtime create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', help='The factory name.')
        c.argument('integration_runtime_name', help='The integration runtime name.')
        c.argument('name', help='The name of the linked integration runtime.')
        c.argument('subscription_id',
                   help='The ID of the subscription that the linked integration runtime belongs to.')
        c.argument('data_factory_name', help='The name of the data factory that the linked integration runtime belongs '
                   'to.')
        c.argument('data_factory_location', help='The location of the data factory that the linked integration runtime '
                   'belongs to.')

    with self.argument_context('datafactory integration-runtime managed create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', help='The factory name.')
        c.argument('integration_runtime_name', options_list=['--name', '-n'], help='The integration runtime name.')
        c.argument('if_match', help='ETag of the integration runtime entity. Should only be specified for update, for w'
                   'hich it should match existing entity or can be * for unconditional update.')
        c.argument('description', help='Integration runtime description.')
        c.argument('factory_vsts_configuration', action=AddFactoryVstsConfiguration, nargs='+', help='Factory\'s VSTS r'
                   'epo information.', arg_group='RepoConfiguration')
        c.argument('factory_git_hub_configuration', action=AddFactoryGitHubConfiguration, nargs='+', help='Factory\'s G'
                   'itHub repo information.', arg_group='RepoConfiguration')
        c.argument('fake_identity', action=AddFakeIdentity, nargs='+', help='This is only for az test.')
        c.argument('zones', nargs='+', help='This is only for az test.')
        c.argument('type_properties_compute_properties', arg_type=CLIArgumentType(options_list=['--type-properties-comp'
                   'ute-properties'], help='The compute resource for managed integration runtime. Expected value: json-'
                   'string/@json-file.'))
        c.argument('type_properties_ssis_properties', arg_type=CLIArgumentType(options_list=['--type-properties-ssis-pr'
                   'operties'], help='SSIS properties for managed integration runtime. Expected value: json-string/@jso'
                   'n-file.'))

    with self.argument_context('datafactory integration-runtime self-hosted create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', help='The factory name.')
        c.argument('integration_runtime_name', options_list=['--name', '-n'], help='The integration runtime name.')
        c.argument('if_match', help='ETag of the integration runtime entity. Should only be specified for update, for w'
                   'hich it should match existing entity or can be * for unconditional update.')
        c.argument('description', help='Integration runtime description.')
        c.argument('type_properties_linked_info', arg_type=CLIArgumentType(options_list=['--type-properties-linked-info'
                   ''], help='The base definition of a linked integration runtime. Expected value: json-string/@json-fi'
                   'le.'))

    with self.argument_context('datafactory integration-runtime update') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', help='The factory name.', id_part='name')
        c.argument('integration_runtime_name', options_list=['--name', '-n'], help='The integration runtime name.',
                   id_part='child_name_1')
        c.argument('auto_update', arg_type=get_enum_type(['On', 'Off']), help='Enables or disables the auto-update feat'
                   'ure of the self-hosted integration runtime. See https://go.microsoft.com/fwlink/?linkid=854189.')
        c.argument('update_delay_offset', help='The time offset (in hours) in the day, e.g., PT03H is 3 hours. The inte'
                   'gration runtime auto update will happen on that time.')

    with self.argument_context('datafactory integration-runtime delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', help='The factory name.', id_part='name')
        c.argument('integration_runtime_name', options_list=['--name', '-n'], help='The integration runtime name.',
                   id_part='child_name_1')

    with self.argument_context('datafactory integration-runtime get-connection-info') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', help='The factory name.', id_part='name')
        c.argument('integration_runtime_name', options_list=['--name', '-n'], help='The integration runtime name.',
                   id_part='child_name_1')

    with self.argument_context('datafactory integration-runtime get-monitoring-data') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', help='The factory name.', id_part='name')
        c.argument('integration_runtime_name', options_list=['--name', '-n'], help='The integration runtime name.',
                   id_part='child_name_1')

    with self.argument_context('datafactory integration-runtime get-status') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', help='The factory name.', id_part='name')
        c.argument('integration_runtime_name', options_list=['--name', '-n'], help='The integration runtime name.',
                   id_part='child_name_1')

    with self.argument_context('datafactory integration-runtime list-auth-key') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', help='The factory name.')
        c.argument('integration_runtime_name', options_list=['--name', '-n'], help='The integration runtime name.')

    with self.argument_context('datafactory integration-runtime regenerate-auth-key') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', help='The factory name.', id_part='name')
        c.argument('integration_runtime_name', options_list=['--name', '-n'], help='The integration runtime name.',
                   id_part='child_name_1')
        c.argument('key_name', arg_type=get_enum_type(['authKey1', 'authKey2']), help='The name of the authentication k'
                   'ey to regenerate.')

    with self.argument_context('datafactory integration-runtime remove-link') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', help='The factory name.', id_part='name')
        c.argument('integration_runtime_name', options_list=['--name', '-n'], help='The integration runtime name.',
                   id_part='child_name_1')
        c.argument('linked_factory_name', help='The data factory name for linked integration runtime.')

    with self.argument_context('datafactory integration-runtime start') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', help='The factory name.', id_part='name')
        c.argument('integration_runtime_name', options_list=['--name', '-n'], help='The integration runtime name.',
                   id_part='child_name_1')

    with self.argument_context('datafactory integration-runtime stop') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', help='The factory name.', id_part='name')
        c.argument('integration_runtime_name', options_list=['--name', '-n'], help='The integration runtime name.',
                   id_part='child_name_1')

    with self.argument_context('datafactory integration-runtime sync-credentials') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', help='The factory name.', id_part='name')
        c.argument('integration_runtime_name', options_list=['--name', '-n'], help='The integration runtime name.',
                   id_part='child_name_1')

    with self.argument_context('datafactory integration-runtime upgrade') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', help='The factory name.', id_part='name')
        c.argument('integration_runtime_name', options_list=['--name', '-n'], help='The integration runtime name.',
                   id_part='child_name_1')

    with self.argument_context('datafactory integration-runtime wait') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('factory_name', help='The factory name.', id_part='name')
        c.argument('integration_runtime_name', options_list=['--name', '-n'], help='The integration runtime name.',
                   id_part='child_name_1')
        c.argument('if_none_match', help='ETag of the integration runtime entity. Should only be specified for get. If '
                   'the ETag matches the existing entity tag, or if * was provided, then no content will be returned.')
