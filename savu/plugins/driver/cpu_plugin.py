# Copyright 2014 Diamond Light Source Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
.. module:: cpu_plugin
   :platform: Unix
   :synopsis: Base class for all plugins which use a CPU on the target machine

.. moduleauthor:: Mark Basham <scientificsoftware@diamond.ac.uk>

"""

from savu.plugins.driver.plugin_driver import PluginDriver


class CpuPlugin(PluginDriver):
    """
    The base class from which all plugins should inherit.
    """

    def __init__(self):
        super(CpuPlugin, self).__init__()

    def run_plugin(self, exp, transport):

        self.run_plugin_instances(transport)
        self._clean_up()
        return
