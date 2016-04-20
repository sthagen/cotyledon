# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import logging

import cotyledon

LOG = logging.getLogger(__name__)


class TestService(cotyledon.Service):
    def __init__(self):
        pass


def example_app():
    logging.basicConfig(level=logging.DEBUG)
    p = cotyledon.ServiceManager()
    p.add_service("processing", TestService, 4)
    p.add_service("reporting", TestService, 1)
    p.run()
