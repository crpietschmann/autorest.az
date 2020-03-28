# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=too-many-lines

import json


def managednetwork_mn_list(cmd, client,
                           resource_group_name=None,
                           top=None,
                           skiptoken=None):
    if resource_group_name is not None:
        return client.list_by_resource_group(resource_group_name=resource_group_name,
                                             top=top,
                                             skiptoken=skiptoken)
    return client.list_by_subscription(top=top,
                                       skiptoken=skiptoken)


def managednetwork_mn_show(cmd, client,
                           resource_group_name,
                           managed_network_name):
    return client.get(resource_group_name=resource_group_name,
                      managed_network_name=managed_network_name)


def managednetwork_mn_create(cmd, client,
                             resource_group_name,
                             managed_network_name,
                             location,
                             tags=None,
                             properties=None):
    if isinstance(properties, str):
        properties = json.loads(properties)
    return client.create_or_update(resource_group_name=resource_group_name,
                                   managed_network_name=managed_network_name,
                                   location=location,
                                   tags=tags,
                                   properties=properties)


def managednetwork_mn_update(cmd, client,
                             resource_group_name,
                             managed_network_name,
                             tags=None):
    return client.begin_update(resource_group_name=resource_group_name,
                               managed_network_name=managed_network_name,
                               tags=tags)


def managednetwork_mn_delete(cmd, client,
                             resource_group_name,
                             managed_network_name):
    return client.begin_delete(resource_group_name=resource_group_name,
                               managed_network_name=managed_network_name)


def managednetwork_scope_assignment_list(cmd, client,
                                         scope):
    return client.list(scope=scope)


def managednetwork_scope_assignment_show(cmd, client,
                                         scope,
                                         scope_assignment_name):
    return client.get(scope=scope,
                      scope_assignment_name=scope_assignment_name)


def managednetwork_scope_assignment_create(cmd, client,
                                           scope,
                                           scope_assignment_name,
                                           location,
                                           assigned_managed_network=None):
    return client.create_or_update(scope=scope,
                                   scope_assignment_name=scope_assignment_name,
                                   location=location,
                                   assigned_managed_network=assigned_managed_network)


def managednetwork_scope_assignment_update(cmd, client,
                                           scope,
                                           scope_assignment_name,
                                           location,
                                           assigned_managed_network=None):
    return client.create_or_update(scope=scope,
                                   scope_assignment_name=scope_assignment_name,
                                   location=location,
                                   assigned_managed_network=assigned_managed_network)


def managednetwork_scope_assignment_delete(cmd, client,
                                           scope,
                                           scope_assignment_name):
    return client.delete(scope=scope,
                         scope_assignment_name=scope_assignment_name)


def managednetwork_managed_network_group_list(cmd, client,
                                              resource_group_name,
                                              managed_network_name,
                                              top=None,
                                              skiptoken=None):
    return client.list_by_managed_network(resource_group_name=resource_group_name,
                                          managed_network_name=managed_network_name,
                                          top=top,
                                          skiptoken=skiptoken)


def managednetwork_managed_network_group_show(cmd, client,
                                              resource_group_name,
                                              managed_network_name,
                                              managed_network_group_name):
    return client.get(resource_group_name=resource_group_name,
                      managed_network_name=managed_network_name,
                      managed_network_group_name=managed_network_group_name)


def managednetwork_managed_network_group_create(cmd, client,
                                                resource_group_name,
                                                managed_network_name,
                                                managed_network_group_name,
                                                location,
                                                management_groups=None,
                                                subscriptions=None,
                                                virtual_networks=None,
                                                subnets=None):
    if isinstance(management_groups, str):
        management_groups = json.loads(management_groups)
    return client.begin_create_or_update(resource_group_name=resource_group_name,
                                         managed_network_name=managed_network_name,
                                         managed_network_group_name=managed_network_group_name,
                                         location=location,
                                         management_groups=management_groups,
                                         subscriptions=subscriptions,
                                         virtual_networks=virtual_networks,
                                         subnets=subnets)


def managednetwork_managed_network_group_update(cmd, client,
                                                resource_group_name,
                                                managed_network_name,
                                                managed_network_group_name,
                                                location,
                                                management_groups=None,
                                                subscriptions=None,
                                                virtual_networks=None,
                                                subnets=None):
    if isinstance(management_groups, str):
        management_groups = json.loads(management_groups)
    return client.begin_create_or_update(resource_group_name=resource_group_name,
                                         managed_network_name=managed_network_name,
                                         managed_network_group_name=managed_network_group_name,
                                         location=location,
                                         management_groups=management_groups,
                                         subscriptions=subscriptions,
                                         virtual_networks=virtual_networks,
                                         subnets=subnets)


def managednetwork_managed_network_group_delete(cmd, client,
                                                resource_group_name,
                                                managed_network_name,
                                                managed_network_group_name):
    return client.begin_delete(resource_group_name=resource_group_name,
                               managed_network_name=managed_network_name,
                               managed_network_group_name=managed_network_group_name)


def managednetwork_managed_network_peering_policy_list(cmd, client,
                                                       resource_group_name,
                                                       managed_network_name,
                                                       top=None,
                                                       skiptoken=None):
    return client.list_by_managed_network(resource_group_name=resource_group_name,
                                          managed_network_name=managed_network_name,
                                          top=top,
                                          skiptoken=skiptoken)


def managednetwork_managed_network_peering_policy_show(cmd, client,
                                                       resource_group_name,
                                                       managed_network_name,
                                                       policy_name):
    return client.get(resource_group_name=resource_group_name,
                      managed_network_name=managed_network_name,
                      managed_network_peering_policy_name=policy_name)


def managednetwork_managed_network_peering_policy_create(cmd, client,
                                                         resource_group_name,
                                                         managed_network_name,
                                                         policy_name,
                                                         location,
                                                         properties=None):
    if isinstance(properties, str):
        properties = json.loads(properties)
    return client.begin_create_or_update(resource_group_name=resource_group_name,
                                         managed_network_name=managed_network_name,
                                         managed_network_peering_policy_name=policy_name,
                                         location=location,
                                         properties=properties)


def managednetwork_managed_network_peering_policy_update(cmd, client,
                                                         resource_group_name,
                                                         managed_network_name,
                                                         policy_name,
                                                         location,
                                                         properties=None):
    if isinstance(properties, str):
        properties = json.loads(properties)
    return client.begin_create_or_update(resource_group_name=resource_group_name,
                                         managed_network_name=managed_network_name,
                                         managed_network_peering_policy_name=policy_name,
                                         location=location,
                                         properties=properties)


def managednetwork_managed_network_peering_policy_delete(cmd, client,
                                                         resource_group_name,
                                                         managed_network_name,
                                                         policy_name):
    return client.begin_delete(resource_group_name=resource_group_name,
                               managed_network_name=managed_network_name,
                               managed_network_peering_policy_name=policy_name)
