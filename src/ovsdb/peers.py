# Copyright 2018 Canonical Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# the reactive framework unfortunately does not grok `import as` in conjunction
# with decorators on class instance methods, so we have to revert to `from ...`
# imports

import inspect

import charmhelpers.core as ch_core

from charms.reactive import (
    Endpoint,
    clear_flag,
    set_flag,
    when,
    when_not,
)


class OVSDBPeers(Endpoint):

    class_var = 'class_value'

    def __init__(self, endpoint_name, relation_ids=None):
        self.instance_var = 'instance_value'
        super().__init__(endpoint_name, relation_ids=relation_ids)


class OVSDBClusterPeers(OVSDBPeers):

    @when('endpoint.ovsdb-peer.broken')
    def broken(self):
        ch_core.hookenv.log('{} -> {} class_var="{}" instance_var="{}"'
                            .format(type(self).__name__,
                                    inspect.currentframe().f_code.co_name,
                                    self.class_var,
                                    self.instance_var),
                            level=ch_core.hookenv.INFO)
