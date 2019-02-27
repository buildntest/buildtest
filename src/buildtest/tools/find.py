############################################################################
#
#  Copyright 2017-2019
#
#  https://github.com/HPC-buildtest/buildtest-framework
#
#  This file is part of buildtest.
#
#  buildtest is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  buildtest is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with buildtest.  If not, see <http://www.gnu.org/licenses/>.
#############################################################################

"""
This module is the entry point for buildtest find subcommand and implements the
following
1. Finds all test (buildtest find --findtest all)
2. Find test by argument (buildtest find --findtest <arg>)
3. Finds all configuration (buildtest find --findconfig all)
4. Find configuration by argument (buildtest find --findconfig <arg>)

"""

import os
import sys
from buildtest.tools.config import config_opts, BUILDTEST_TEST_EXT
from buildtest.tools.file import walk_tree, walk_tree_multi_ext

def func_find_subcmd(args):
    """ This is the entry method for find subcommand."""

    if args.findconfig == "all":
        find_all_yaml_configs()
    if args.findconfig:
        find_yaml_configs_by_arg(args.findconfig)
    if args.findtest == "all":
        find_all_tests()
    if args.findtest:
        find_tests_by_arg(args.findtest)

    sys.exit(0)

def find_all_yaml_configs():
    """ This method find all yaml configuration."""

    yml_files = walk_tree(config_opts['BUILDTEST_CONFIGS_REPO'],".yml")
    for f in yml_files:
        print(f)
    print (f"Total YAML Configuration Files: {len(yml_files)}")



def find_yaml_configs_by_arg(find_arg):
    """This method find yaml configuration based on argument."""
    count = 0

    yml_files = walk_tree(config_opts['BUILDTEST_CONFIGS_REPO'],".yml")

    for file in yml_files:
        if find_arg in os.path.basename(file):
            print(file)
            count+=1
    print (f"Total YAML configs: {count}")


def find_all_tests():
    """This method finds all test scripts in BUILDTEST_TESTDIR. """
    test_list = walk_tree_multi_ext(config_opts["BUILDTEST_TESTDIR"],
                                    BUILDTEST_TEST_EXT)
    for test in test_list:
        print(test)
    print (f'{len(test_list)} Test scripts found in " + '
           f'{config_opts["BUILDTEST_TESTDIR"]}')


def find_tests_by_arg(find_arg):
    """find all test scripts in $BUILDTEST_TESTDIR"""
    count = 0

    test_list = walk_tree_multi_ext(config_opts['BUILDTEST_TESTDIR'],
                                    BUILDTEST_TEST_EXT)
    for test in test_list:
        if find_arg in os.path.basename(test):
            print(test)
            count+=1
    print (f"{count} Test found with name {find_arg} in its filename")

