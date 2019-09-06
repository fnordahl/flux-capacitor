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

import lib


ch_core.hookenv.log('MODULE: {}'.format(__name__), level=ch_core.hookenv.INFO)


class OVSDBProvides(Endpoint):

    class_var = 'class_value'

    def __init__(self, endpoint_name, relation_ids=None):
        super().__init__(endpoint_name, relation_ids=relation_ids)
        self.instance_var = 'OVSDBProvides_instance_value'


class OVSDBClusterProvides(OVSDBProvides):

    def __init__(self, endpoint_name, relation_ids=None):
        super().__init__(endpoint_name, relation_ids=relation_ids)
        self.instance_var = 'OVSDBClusterProvides_instance_value'

    @when('endpoint.ovsdb.joined')
    def joined(self):
        ch_core.hookenv.log('{}: {} -> {} class_var="{}" instance_var="{}"'
                            .format(self._endpoint_name,
                                    type(self).__name__,
                                    inspect.currentframe().f_code.co_name,
                                    self.class_var,
                                    self.instance_var),
                            level=ch_core.hookenv.INFO)
        lib.my_func()

    @when_any('endpoint.ovsdb.broken')
    def broken(self):
        ch_core.hookenv.log('{}: {} -> {} class_var="{}" instance_var="{}"'
                            .format(self._endpoint_name,
                                    type(self).__name__,
                                    inspect.currentframe().f_code.co_name,
                                    self.class_var,
                                    self.instance_var),
                            level=ch_core.hookenv.INFO)
