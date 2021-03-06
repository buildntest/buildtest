CHANGELOG
=========

v0.9.2 (Jan 12th, 2021)
-----------------------

In this version, we added significant changes to ``compiler-v1.0-schema.json`` to support compiler test. This includes
ability for building a single test across multiple compiler instance and across compiler groups (gcc, intel, cray, etc...) User
can search compilers via regular expression when building test, and specify setting common to compiler group or shared across all 
compilers. In addition, one can override properties at the compiler level. 

This version introduced significant refactor in codebase responsible for building, running and buildspec operation. We introduce
classes when appropriate. We added a Gitlab `CI job <https://github.com/buildtesters/buildtest/blob/devel/.gitlab-ci.yml>`_ at Cori 
to run regression test and report coverage report to codecov. This pipeline is run manually and  functionality will change until 
we have stable environment for running PR pipelines.

We changed the behavior of ``buildtest build --tags`` previously it was used for discovering buildspecs
and filtering test, now it only discovers test. A new option was added ``--filter-tags`` which
is used for filtering tests by tagname. Previously if one used ``--tags`` with ``--buildspec`` or
``--executor`` would result in filtered tests by tags and buildtest may ignore some tests that
were expected to run. With this change we can better support both use-case where one wants to discover
tests by tag and filter them. This was implemented in `#587 <https://github.com/buildtesters/buildtest/pull/587>`_.

- Refactor implementation for ``buildtest report`` into class see `#555 <https://github.com/buildtesters/buildtest/pull/555>`_
- The ``module`` property is changed from ``array`` to ``object`` type which allows one to specify ``module load``, ``module swap``, ``module purge``. See `#556 <https://github.com/buildtesters/buildtest/pull/556>`_
- Fix bug in slurm job when executor was indefinitely polling jobs in ``TIMEOUT`` and ``OUT_OF_MEMORY`` job state. See `#561 <https://github.com/buildtesters/buildtest/pull/561>`_.
- Increase test coverage for ``buildtest inspect`` and searching compilers see `#575 <https://github.com/buildtesters/buildtest/pull/575>`_.


v0.9.1 (Nov 24th, 2020)
------------------------

In this version, we added support for `Cobalt scheduler <https://trac.mcs.anl.gov/projects/cobalt>`_ provided by
Argonne National Laboratory. We can define cobalt executors in buildtest settings which can be
mapped to cobalt queues. There is a ``cobalt`` property for adding **#COBALT** directives
into test script. Some of the cobalt options are mapped to ``batch`` field for scheduler
agnostic configuration.

In this version we added support for compiler query and detection using ``buildtest config compilers find``.
We make use of `lmodule <http://lmodule.rtfd.io/>`_ API for querying modules if system
is using Lmod.

We made significant changes to buildspec cache file (``var/buildspec-cache.json``) that allowed
us to add several options to ``buildtest buildspec find`` including: ``--group-by-tags``,
``--group-by-executor``, ``--paths``, ``--helpformat``, ``--format``, ``--helpfilter``, ``--filter``, ``--root``.

There was significant code refactor to several class and issues reported by CodeFactor. In addition we added
CI checks such as **Daily Check URL** see `eb601b <https://github.com/buildtesters/buildtest/commit/eb601b4610a32b8f41cf919f5e6877584247d869>`_,
gh-pages for master branch see `267f7f <https://github.com/buildtesters/buildtest/commit/267f7f913cd8e1b5303b1af42aa307bfe76ee3bf>`_. The gh-pages
for JSON schema push documentation for `devel` and `master` in separate sub-directories. This allows user to view schema examples and markdown
pages for schema for devel and master branch.

- Add new maintainers checklist guide see `#529 <https://github.com/buildtesters/buildtest/pull/529>`_
- Rename ``--clear`` --> ``--rebuild``, ``--list-executors`` --> ``--executors`` in **buildtest buildspec find** see `e7ec37 <https://github.com/buildtesters/buildtest/commit/e7ec378389dfa9b9e07e98eaf4c0990b958a2177>`_
- Added property ``moduletool`` in settings schema for configuring module system
- Add property ``load_default_buildspecs`` in settings schema for configuring buildtest to load default buildspecs in buildspec cache. See commit `dac444 <https://github.com/buildtesters/buildtest/commit/dac4444b42a07b5c8f281dd0458df09e08e75383>`_
- Remove property ``editor`` from settings schema and ``buildtest buildspec view`` and ``buildtest buildspec edit`` were deprecated see `b8479b <https://github.com/buildtesters/buildtest/commit/b8479b4b0b3da9eaeae95ba06c2b4458986e57cf>`_
- Fix bug during job timeout in poll stage. Buildtest will ignore cancelled jobs, but there no check if no builders were returned after poll stage. See `#532 <https://github.com/buildtesters/buildtest/pull/532>`_
- Add Burst Buffer (``BB``) and Data Warp (``DW``) directives for Cray support. See `#525 <https://github.com/buildtesters/buildtest/pull/525>`_ and `#526 <https://github.com/buildtesters/buildtest/pull/526/>`_
- Add csh, tcsh, zsh shell support in script-v1.0.schema.json `#523 <https://github.com/buildtesters/buildtest/pull/523>`_


v0.9.0 (Oct 21st, 2020)
------------------------

The major changes in v0.9.0 are the following

First we moved schema development from https://github.com/buildtesters/schemas
into buildtest and add custom RefResolver for validating schemas on local
filesystem as pose to fully qualified URI.

We host schema, examples, and schema docs on Github pages at
https://buildtesters.github.io/buildtest/ by adding a `jsonschemadocs <https://github.com/buildtesters/buildtest/blob/devel/.github/workflows/jsonschemadocs.yml>`_ workflow.
We moved JSON definitions to separate file called `definitions.schema.json`.

We added `setup.sh`, `setup.csh` script to install buildtest for bash/csh shells,
this now changes the way we install buildtest as pose to using **pip**.
We introduced scheduler agnostic configuration using ``batch`` field.
This property currently translates a subset of options for Slurm and LSF.
We have added generic tests to buildtest in top-level folder `generic-tests`
which is an attempt to provide buildspecs that anyone can use. Currently, these
tests are run using Local Executors. We added the properties ``account``
and ``max_pend_time`` in executor configuration. The ``account`` field is used for
sites to specify a project account to charge resource, this can be set default on
all executors or defined per executor setting. The ``max_pend_time`` is
**maximum time limit job can stay pending in executor queue**, this was an enhancement
from previous model where jobs can run indefinitely without any cancellation option.

- Add new command ``buildtest inspect`` to view test details see `#516 <https://github.com/buildtesters/buildtest/pull/516>`_
- Disable Travis and enable codecov comments see `#519 <https://github.com/buildtesters/buildtest/pull/519>`_
- Add `account` field in buildtest setting to specify job account, this can be set default on all batch executors or set within executor scope which overrides default. See `#514 <https://github.com/buildtesters/buildtest/pull/514>`_
- Add `max_pend_time` in buildtest settings to cancel job if its in pending state. This was tested for Slurm and LSF scheduler.  See `#509 <https://github.com/buildtesters/buildtest/pull/509>`_, `#510 <https://github.com/buildtesters/buildtest/pull/510>`_
- Add option ``buildtest schema --validate`` to validate example schemas. The option ``buildtest schema --example`` shows content of schema examples see `#502 <https://github.com/buildtesters/buildtest/pull/502>`_
- Deprecate command ``buildtest config edit`` see `#512 <https://github.com/buildtesters/buildtest/pull/512>`_
- Fix bug when retrieving tags with command ``buildtest buildspec find --tags`` see `#501 <https://github.com/buildtesters/buildtest/pull/501>`_
- Add scheduler agnostic configuration via ``batch`` field see `#493 <https://github.com/buildtesters/buildtest/pull/493>`_ and `#494 <https://github.com/buildtesters/buildtest/pull/494>`_
- Add a ``setup.sh``, ``setup.csh`` script to install buildtest. This changes the way buildtest is installed as pose to using **pip** see `#491 <https://github.com/buildtesters/buildtest/pull/491>`_ `#503 <https://github.com/buildtesters/buildtest/pull/503>`_
- Add a custom RefResolver for resolving JSON schemas in filesystem as pose to using public URL, this was important for testing schema changes locally which was not present before. See `#487 <https://github.com/buildtesters/buildtest/pull/487>`_
- The ``returncode`` field can be a string or a list for matching returncode status. The `tags` field can be a string or list of strings, before it could only be a list.  See `#486 <https://github.com/buildtesters/buildtest/pull/486/>`_
- Migrate schema development from https://github.com/buildtesters/schemas into main project.  see `#480 <https://github.com/buildtesters/buildtest/pull/480>`_
- Fix bug when when writing python scripts in ``run`` section, we add stage/run directory in test destination directory see `#477 <https://github.com/buildtesters/buildtest/pull/477/>`_.


v0.8.1 (Sep 14th, 2020)
-----------------------

- We now running regression test in github action see `#455 <https://github.com/buildtesters/buildtest/pull/455>`_
- Add command to filter by executor names using ``buildtest build --executor``. `#463 <https://github.com/buildtesters/buildtest/pull/463>`_
- Add option for filtering buildspec cache using ``buildtest buildspec find --filter`` and see list of available filter option using  ``buildtest buildspec find --helpfiler`` see `#464 <https://github.com/buildtesters/buildtest/pull/464>`_
- Support for building with multiple tags `#462 <https://github.com/buildtesters/buildtest/pull/462>`_
- Add option for filtering test report using ``buildtest report --filter`` option and ``buildtest report --helpfilter`` with list of filter fields. See `#449 <https://github.com/buildtesters/buildtest/pull/449>`_
- Add option for ``buildtest --docs`` and ``buildtest --schemadocs`` to access documentation through CLI. See `#452 <https://github.com/buildtesters/buildtest/pull/452>`_
- Retrieve a list of unique executors (``buildtest buildspec find --list-executors``) from buildspec cache see `#448 <https://github.com/buildtesters/buildtest/pull/448>`_
- Query buildspec tags and buildspec files using ``buildtest buildspec find --tags`` and ``buildtest buildspec find --buildspec-files`` option see `#445 <https://github.com/buildtesters/buildtest/pull/445>`_


v0.8.0 (Sep 3rd, 2020)
-----------------------
 
This release includes major changes to framework, in particular we use `jsonschema <https://json-schema.org/>`_ to 
validate schemas and add separate repository: https://github.com/buildtesters/schemas for development of schemas. The 
schemas are hosted in Github pages at https://buildtesters.github.io/schemas/schemadocs/. There are four main schemas:
**global.schema.json**, **script-v1.0.schema.json**, **compiler-v1.0.schema.json**, and **settings.schema.json**. The **settings.schema.json**
is used for configuring buildtest. The global.schema.json is used for validating global section of buildspec and sub-schema
script-v1.0.schema.json and compiler-v1.0.schema.json are used for validating test section. These are used when ``type: script``
or ``type: compiler`` is set.

All tests are run via executors defined in buildtest configuration, currently we support LocalExecutor, LSFExecutor, and SlurmExecutor
for submitting jobs to local host, LSF and Slurm scheduler. As part of this release, we removed all features related to buildtest modules
and they are now part of a Python API called `lmodule <https://github.com/buildtesters/lmodule>`_ which is a separate project.

At high level the following commands were introduced: ``buildtest build``, ``buildtest buildspec``, ``buildtest schema``, ``buildtest config``,
and ``buildtest report``. To build any buildspecs use the **buildtest build** command, main options are ``buildtest build --buildspec`` which 
takes input file or directory. You can use ``buildtest build --exclude`` to exclude buildspec files. Both options can be specified multiple times.
buildtest can search buildspecs by tags when building them using ``buildtest build --tags <TAGNAME>``. This feature assumes you a buildspec cache 
which can be populated using ``buildtest buildspec find``. This command discovers and validates all buildspecs and invalid buildspecs are reported
in file. The ``buildtest buildspec view`` and ``buildtest buildspec edit`` can view or edit a buildspec file provided you specify name of buildspec.

The ``buildtest schema`` command provides access to schemas and examples, if you run ``buildtest schema`` it will display all schema names, you can
select a schema using ``buildtest schema -n <schema>`` with option ``--examples`` or ``--json`` to view schema examples or json file. The 
``buildtest config`` command is used showing buildtest configuration, you can view buildtest configuration using ``buildtest config view`` and 
validate the configuration with schema using ``buildtest config validate``. The ``buildtest config edit`` can be used to open configuration using
an editor and validate configuration upon closing file. If file is not valid, buildtest will print message exception from **jsonschema.validate**
to stdout and open file again. This process happens in a while loop until user has validated the configuration. The ``buildtest report`` command is 
used for showing test reports. The output can be filtered using ``buildtest report --format`` to select fields which alter the column outputs. 
The available fields can be retrieved using ``buildtest report --helpformat``. 

In this release, we added significant coverage to regression tests and organize tests such that source directory (`buildtest`) mirrors to test directory
(`tests`) for instance testing module ``buildtest.menu.build`` will have a test in ``tests/menu/test_build.py``. buildtest comes with a set of example 
tests meant to serve as a tutorial for buildtest. These tests are toy examples meant to augment documentation examples and serve as means to automate
documentation examples or used in regression tests.

- Add Github Issue Templates 
- Remove workflow Issue Label Bot
- Add pyflakes check in black workflow
- Add TutorialsValidation workflow for validating buildspecs 
- Change First Issue Greeting workflow to run only on first issue and not for pull request
- Upgrade version of urlcheck workflow changed from ``SuperKogito/URLs-checker@0.1.2`` --> ``urlstechie/urlchecker-action@0.2.1``
- Add pre-commit hook to automate python format via ``black``. Add ``black --check`` as automated check see `#172 <https://github.com/buildtesters/buildtest/pull/172>`_, `#179 <https://github.com/buildtesters/buildtest/pull/179>`_
- Remove black pre-commit file ``.github/hooks/pre-commit`` in replacement for ``.pre-commit-config.yaml`` that installs the pre-commit file
- Remove Lmod installation from Travis since buildtest doesn't depend on Lmod anymore
- Rename GitHub Organization from ``HPC-buildtest`` to ``buildtesters`` and update links throughout documentation
- Update License Copyright from ``2017-2019`` to ``2017-2020`` and add `Vanessa Sochat <https://github.com/vsoch>`_
- Add more badges in README.rst and updates to file
- We can retrieve tags and buildspec files from cache using ``buildtest buildspec find --tags`` and ``buildtest buildspec find --buildspec-files`` see
- Add logging support via python `logging <https://docs.python.org/3/library/logging.html>`_ library. Logs are written to file and they can be
  streamed to stdout using **buildtest -d <DEBUGLEVEL>**
- Use `sphinx-autoapi <https://sphinx-autoapi.readthedocs.io/en/latest/index.html>`_ to automate api docs instead of using `sphinx.ext.autodoc <https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html>`_
- Add documentation for Contributing Guide, Maintainer guide, Github Integration, and Regression Testing
- Add tox.ini file for automating python tests using `tox <https://tox.readthedocs.io/en/latest/>`_
- Remove CLI option ``buildtest build [run|log|test]`` see `#163 <https://github.com/buildtesters/buildtest/pull/163>`_
- Remove all module operations and cli menu ``buildtest module``. This is now moved to an API lmodule at https://github.com/buildtesters/lmodule
- removing extra dependencies argcomplete and termcolor
- removing bash script and sourcing in favor of Python module install

v0.7.6 (Feb 4th, 2020)
-----------------------

- Add GitHub actions: ``greetings``, `trafico <https://github.com/marketplace/trafico-pull-request-labeler>`_, `URLs-checker <https://github.com/marketplace/actions/urls-checker>`_, `pull-request-size <https://github.com/marketplace/pull-request-size>`_ 
- Add `coveralls <https://github.com/marketplace/coveralls>`_ for coverage report 
- Use `Imgbot <https://github.com/marketplace/imgbot>`_ bot to convert all images via lossless compression to reduce image size
- Update ``.gitignore`` file to reflect file extension relevant to buildtest 
- Remove command option ``buildtest testconfigs maintainer`` and benchmark feature ``buildtest benchmark``
- Rename output style when showing buildtest configuration (``buildtest show --config``)
- Add option to list all parent modules ``buildtest module --list-all-parents``
- Move code base  from ``src/buildtest`` --> ``buildtest`` and move ``buildtest`` script --> ``bin/buildtest``
- Update contributing docs, and upload slides from 5th Easybuild User Meeting and FOSDEM20 

v0.7.5 (Dec 31st, 2019)
-----------------------

- Major improvement to Travis build. buildtest will now test for python ``3.6``, ``3.7``, ``3.8`` for Lmod version ``6.6.2`` and ``7.8.2``
- Travis will install easybuild and setup a mini software stack that is used for by regression test
- Port the regression test to comply with Travis build environment and ``coverage`` report automatically get pushed to CodeCov
- Removing subcommand ``buildtest benchmark [hpl | hpcg]``
- Add options to ``buildtest module loadtest`` to control behavior on module loadtest.
- buildtest can run module loadtest in a **login shell** via ``buildtest module loadtest --login`` and restrict number of
  test using ``--numtest`` flag. buildtest will automatically purge modules before loading test but this can be tweaked
  using ``--purge-modules`` flag
- Remove command ``buildtest list`` and remove implementation for retrieving easyconfigs ``buildtest list --easyconfigs``
- Option ``buildtest list --software`` is now ``buildtest module --software`` and ``buildtest list --modules`` is now ``buildtest module list``
- Add the following flags: ``--exclude-version-files``, ``--filter-include``, ``--querylimit`` to ``buildtest module list``
  to tweak behavior on module list
- Update buildtest configuration (``settings.yml``) with equivalent **key/value** to control behavior of ``buildtest module [list | loadtest]``.
  The configuration values are overridden by command line flags
- buildtest will ignore ``.version``, ``.modulerc`` and ``.modulerc.lua`` files when reporting modules in ``buildtest module list``. This
  is controlled by ``exclude-version-files`` in configuration or flag ``--exclude-version-files``
- Remove sanity check feature ``buildtest build --package`` and ``buildtest build --binary`` and remove configuration ``BUILDTEST_BINARY`` from configuration file
- Remove option ``buildtest build --parent-module-search`` and remove ``BUILDTEST_PARENT_MODULE_SEARCH`` from configuration file
- Update documentation procedure regarding **installation of buildtest** and remove **Concepts** page


v0.7.4 (Dec 11th, 2019)
-------------------------

- update documentation section **Background**, **Motivation**, **Inception**, and **Description**
- make use of ``$SRCDIR`` when setting variable ``SRCFILE`` in test script.
- add documentation issue template page
- add clang compiler support via ``compiler:clang``
- add contributing pages to buildtest documentation and add further clarification on release process, buildtest regression testing, and GitHub app integration
- add ``EDITOR`` key in buildtest configuration (**settings.yml**) to tweak editor when editing files
- change path to output/error files in ``buildtest module loadtest`` and print actual ``module load`` command
- adding github stalebot configuration see ``.github/stale.yml``
- adding github sponsor page ``.github/FUNDING.yml``
- add stream benchmark test see `d2a2a4 <https://github.com/buildtesters/buildtest/commit/d2a2a4dc2e71c5921b211d4df4d68b7f52cbbf52>`_
- adding github workflow ``black`` to format all python code base see ``.github/workflow/black.yml``
- install lmod and its dependency in travis build


v0.7.3 (Nov 25th, 2019)
-----------------------

- enable ``cuda``, ``intel``, ``pgi`` compilation, this can be set via ``compilers`` key
- Define shell variables ``CC``, ``FC``, ``CXX`` to be used to reference builds
- Define shell variable ``EXECUTABLE`` to reference generated executable
- Fix Code Style issues reported by CodeFactor (https://www.codefactor.io/repository/github/buildtesters/buildtest)
- Add , hust-19 slides, buildtest architecture and workflow diagram in documentation
- Simplify output of ``buildtest module --easybuild`` and ``buildtest module --spack``
- Add ``module purge`` or ``module --force purge`` in test (`#122 <https://github.com/buildtesters/buildtest/issues/122>`_)
- automate documentation examples for building test examples
- move all documentation examples to ``toolkit/suite/tutorial``
- update CONTRIBUTING.rst guide to include section on building buildtest API docs, automating documentation examples and running regression test via pytest


v0.7.2 (Nov 8th, 2019)
----------------------
- automate documentation test generation using python script
- add support for coverage see https://codecov.io/gh/buildtesters/buildtest
- adding dry option when building tests (short: ``-d`` or long option:``--dry``)
- automate buildtest testing process via pytest. Add initial support with 25+ regression tests
- adding directory expansion support when files or directory are references such as $HOME or tilde (~) operation
- adding several badges to README.rst

v0.7.1 (Oct 30th, 2019)
---------------------
- Re-implement core mechanics of the build framework by using new YAML schema.
- Release buildtest under MIT license
- Yaml schema can be printed via ``buildtest show -k singlesource``. The schema provides building
  C, C++, Fortran code along with MPI test. Provides keys such as ``cflags``, ``cxxflags``, ``fflags``
  ``cppflags``, ``ldflags`` for passing compiler options. The schema provides a dictionary to
  insert **#BSUB** and **#SBATCH** directives into job scripts via ``bsub:`` and ``sbatch:`` keys.
- Add documentation example on C, C++, Fortran, MPI, and OpenACC code.
- Add options **buildtest build bsub** (bsub wrapper) such as ``-n``, ``-W``, ``-M``,``-J``,``--dry-run``.
- Add key TESTDIR in **build.json** to identify test directory, this makes it easier when running test


v0.7.0 (Oct 16th, 2019)
----------------------
- autodetect slurm configuration from system and write to json file
- add option ``buildtest module --module-deps`` that prints modules dependent on parent modules
- add subparser ``buildtest module tree`` that provides operation for managing module trees (**BUILDTEST_MODULEPATH**)
- remove subparser ``buildtest find``
- add option ``buildtest build --collection`` for building test with Lmod user collection
- remove option ``buildtest build --software``
- add option ``buildtest build --modules`` which allows test to be build with multiple module versions
- add option ``buildtest module collection`` for managing module collection using buildtest. Alternative to Lmod user collection
- remove option ``buildtest --clean-logs``
- Color output of Lua and non-lua modules in ``buildtest list --modules``.
-  Remove option ``--python-package``, ``--perl-package``, ``--ruby-package``, ``--r-package`` from **build** menu. Also delete all reference in documentation and delete repository
- ``--buildtest-software`` option is removed
- ``--format`` option in list submenu only supports **json**. Previously it also supported **csv**
- Rename all test scripts for documentation and rst files to be lower case
- Convert CONTRIBUTING guide from Markdown to Restructured Text (RsT) and add Contributing section in documentation
- Change buildtest config file path to be $HOME/.buildtest/settings.yml
- Use sphinx-argparse to automate argparse documentation
- Rename main program **_buildtest** to **buildtest** and changed source code directory layout
- Add option ``-b`` or ``--binary`` for native support for sanity check on binary commands in framework without using yaml files
- Update requirements.txt
- Migrate documentation to buildtest
- Create subcommand **find** and move option ``-ft`` and ``-fc`` to this menu
- Add logo for license, version, download, status to README.rst
- Type checking support for buildtest configuration file
- Remove option ``--output`` from **run** submenu
- Add support for OSU Benchmark  and add this to benchmark submenu and document this page
- Add threshold value for running test. This can be configured using BUILDTEST_SUCCESS_THRESHOLD
- Create submenu ``module`` and move option ``--diff-trees`` and ``--module-load-test`` to this menu

v0.6.3 (Oct 26th, 2018)
----------------------------
- OpenHPC yaml files are moved from $BUILDTEST_CONFIGS_REPO/ohpc to  $BUILDTEST_CONFIGS_REPO/buildtest/ohpc
- This led to minor fix on how buildtest will write yaml files via ``_buildtest yaml --ohpc`` and build tests via ``_buildtest build --ohpc``
- Add OpenHPC integration with buildtest with option ``--ophc``. This is available for ``build`` and ``yaml`` subcommand
- Rename option ``--ignore-easybuild`` to ``--easybuild``. When this is set, buildtest will check if software is easybuild software.
- BUILDTEST_EASYBUILD and BUILDTEST_OHPC can be defined in configuration file or environment variable
- Fix sorting issue with output for ``_buidltest list -svr`` and ``_buildtest list -bs``
- Add option ``--prepend-modules`` that can prepend modules to test script before loading application module.
- buildtest will now ignore all .version* files as pose to .version file, this is due to Lmod 7 and how OpenHPC module files have hidden modules with format .versionX.Y.Z
-

v0.6.1 (Oct 18th, 2018)
---------------------------
- Fix issue with pypi package dependency in version 0.6.0

v0.6.0 (Oct 17th, 2018)
---------------------------
- **New Feature:** option to build all software and system packages using ``--all-software`` and ``--all-package``
- **New Feature:** option to build all yaml configuration for software and system package using ``--all-software`` and ``--all-package``
- **New Feature:** option to run all tests for software and system package using ``--all-software`` and ``--all-package``
- **New Feature:** add option ``--output`` to control output  for test execution. Output can be redirected to /dev/null or /dev/stdout
- rename option ``--system`` to ``--package``
- option ``--software`` and ``--package`` is consistent across build, yaml, and run subcommand
- Add test count, passed and failed test after each test run when using ``_buildtest run``.
- option ``--rebuild`` and ``--overwrite`` will work with ``--all-software`` and ``--all-package`` in yaml subcommand to automate rebuilding of yaml files
-  Move option `--module-naming-scheme`  to build subcommand
- **bug fix:** directory issue for running buildtest first time https://github.com/buildtesters/buildtest/issues/81
- **bug fix:** print error https://github.com/buildtesters/buildtest/issues/80

v0.5.0 (Oct 8th, 2018)
-----------------------

- **New Feature:** Add new sub-commands ``build`` ``list`` ``run`` to buildtest
- Move the following options to ``build`` sub command
   - ``-s``
   - ``-t``
   - ``--enable-job``
   - ``--job-template``
   - ``--system``
   - ``--r-package-test``
   - ``--python-package-test``
   - ``--perl-package-test``
   - ``--ruby-package-test``
   - ``--shell``
   - ``--ignore-easybuild``
   - ``--clean-tests``
   - ``--testdir``
   - ``--clean-build``
- Move the following option to ``list`` sub command
  - ``-ls``
  - ``-lt``
  - ``-svr``
- Add option ``--format`` in ``list`` sub command to view output in ``csv``, ``json``. Default is ``stdout``
- Add the following option to ``run`` sub command
   - ``--app``
   - ``--systempkg``
   - ``--interactive`` (originally ``--runtest``)
   - ``--testname``
- Added basic error handling support
- Add ``description`` key in all yaml files
-  Tests have permission ``755`` so they can run automatically as any user see `6a2570 <https://github.com/buildtesters/buildtest/pull/79/commits/6a2570e9d547b0fb3ab81a14770583a192092224>`_
- Options for ``--ebyaml`` now generates date-time stamp for ``command.yaml`` see `a59682 <https://github.com/buildtesters/buildtest/pull/79/commits/a5968263e4faeac0b65386b22d9b1d5cff604185>`_
- Add script ``check.sh`` to automate testing of buildtest features and package building for verification

v0.4.0 (Sep 11th, 2018)
--------------------------

- Must use Python 3.6 or higher to use this version. All versions < 0.4.0 are supported by Python 2.6 or higher

v0.3.0 (Aug 7th, 2018)
----------------------------------

- Package buildtest as pypi package, now it can be installed via ``pip install buildtest``
- Rename ``buildtest`` to ``_buildtest`` and all code is now under ``buildtest``
- All buildtest repos are now packaged as pypi package and test are moved under `buildtest` directory
- The option `--ebyaml` is now working with auto-complete feature and ability to create yaml files for software packages
- Binary test are now created based on unique sha256sum see `92c012 <https://github.com/buildtesters/buildtest/commit/92c012431000ff338532a899e3b5f465f18786dd>`_
- Output of `--scantest` has been fixed and added to documentation
- Add singularity CDASH script, need some more work on getting server setup properly

New options
~~~~~~~~~~~~~
- `--r-package`: build test for r packages
- `--python-package`: build test for python packages
- `--perl-package:` build test for perl packages
- `--ruby-package`: build test for ruby packages
- `--show-keys` : Display description of yaml keys

- The option `--testset` is removed and will be replaced by individual option for r, perl, python, ruby package options


Bug Fixes
~~~~~~~~~~~~~

- Fix issue with `--runtest` option, it was broken at some point now it is working as expected
- Add extra configuration option in `config_opts` to reuse variable that were needed throughout code and fix bug with `--sysyaml` see `493b53 <https://github.com/buildtesters/buildtest/commit/493b53e4cfdb5710b384409edc7c85ceb05395ba>`_.
- Fix bug with directory not found in menu,py by moving function `check_configuration` and `override_configuration` from main.py to menu,py see `d2c780 <https://github.com/buildtesters/buildtest/commit/d2c78076eb551683bf81a3a7d12ae10971460971>`_

v0.2.0 (May 18th, 2018)
---------------------------

This is a major release update on buildtest with additional options and most importantly
ability to test software stack without easybuild. buildtest can be used to test multiple
software trees, with ability to disable easybuild check for software stack built without
easybuild. The easybuild verification in buildtest has been simplified and it can easily
report which software is built by easybuild.

buildtest can report difference between 2 module trees and multiple module trees can be
specified at same time for building test, and listing software, and software-version.
There has been some improvement on how buildtest operates with ``Flat-Naming-Scheme (FNS)``
module naming scheme for module tree. Basically you don't need to use ``--toolchain``
option with buildtest if you are using ``FNS`` naming scheme but for ``HMNS``
module tree you will need to use ``--toolchain`` option

- Add short option ``-mns`` for ``--module-naming-scheme`` and report total count for software, toolchain and software-version for options ``-ls``, ``-lt``, ``-svr``
- Adding options ``--clean-logs``, ``--clean-tests`` for removing directories via command line
- The file ``config.yaml`` is used to modify buildtest configuration and users can modify this to get buildtest working.
- Environment variables can override configuration in ``config.yaml`` to allow further flexibility
- add option ``--logdir`` to specify alternate path from the command line
- remove option ``--check-setup``
- buildtest can operate on multiple module trees for option ``-ls`` and ``-svr``
- rename option ``--modules-to-easyconfigs`` to ``--easyconfigs-to-moduletrees`` with a short option ``-ecmt``
- add option to show difference between module trees using ``--diff-tree``
- Fixed a bug where ``.version`` files were reported in method ``get_module_list``
- Add option ``--ignore-easybuild`` to disable easybuild check for a module tree
- rename buildtest variables in source code
- add option ``--show`` to display buildtest configuration
- add option ``--enable-job`` to enable Job integration with buildtest this is used with options ``--job-template``
- rename all sub-directories in repo ``BUILDTEST_CONFIGS_REPO`` to lowercase to allow buildtest to generate tests if software is lower case such as ``gcc`` and ``GCC`` in the module file. This enables buildtest to operate with module trees that dont follow easybuild convention
- buildtest will only generate tests for packages in python, R, ruby, perl when using ``--testset`` option if software has these packages installed. This avoids having to create excess test when they are bound to fail
- ``--testset`` option now works properly for both ``HMNS`` and ``FNS`` module naming scheme and is able to operate on modules that don't follow easybuild module naming convention

v0.1.8 (Jan 8th, 2018)
------------------------

- Automate batch job submission from buildtest via **--submitjob**
- Fix shell magic (#!/bin/sh, #!/bin/bash, #!/bin/csh) for binary test
- Tab completion for buildtest argument using ``argcomplete`` module. See `ddb9e4 <https://github.com/buildtesters/buildtest/pull/52/commits/ddb9e426f1b466d3e9b1957a009f0955c236f7a2>`_
- autopopulate choice for ``--system``, ``--sysyaml``, and ``--software``
- Fix output of ``-svr`` and resolve bug when 2 modules with same app/version found in different trees. Only in HMNS. See ` 7ddf91 <https://github.com/buildtesters/buildtest/pull/52/commits/7ddf91b761f88ddacf0548c7f259b2badd93bdfd>`_ for more details
- Group buildtest commands for ease of use.
- Support for yaml keys **scheduler** and **jobslot** to enable jobscript creation from yaml files. See `0fe418 <https://github.com/buildtesters/buildtest/pull/52/commits/0fe4189df0694bef586e9d8e4565ec4cc3e169c9>`_
- Further support for scheduler and automatic detection. Currently supports LSF and SLURM.

v0.1.7 (Nob 28th, 2017)
------------------------

- Add support for creating LSF Job scripts via templates. Use **buildtest --job-template** see `927dc0 <https://github.com/buildtesters/buildtest/commit/927dc09e347fdafa7020d7cfd3016fd8f430ac10>`_
- Add support for creating YAML config for system package binary testing  via **buildtest --sysyaml** see `4ab887 <https://github.com/buildtesters/buildtest/commit/4ab8870eddb9da5177b6c414e98f1231d14b35ab>`_
- adding keys envvar, procrange, threadrange in YAML `9a2152 <https://github.com/buildtesters/buildtest/commit/9a2152307dbf88943618a0b7ee8f6984de3a5340>`_ `152423 <https://github.com/buildtesters/buildtest/commit/1524238919be638edc831df6395425f92e46bc2c>`_ `3d43b8 <https://github.com/buildtesters/buildtest/commit/3d43b8a68946c4a376e1645c4ad204c7498ae6c3>`_
-  Add support for multiple shell (csh, bash, sh) see `aea9d6 <https://github.com/buildtesters/buildtest/commit/aea9d6ff06dcc207e84ba0953c53e2cbd67a49fe>`_ `c154db <https://github.com/buildtesters/buildtest/commit/c154db87f876251cc6b2985e8bfb8c2265843216>`_
- remove verbose option from buildtest
- major code refactor see `fd8d46 <https://github.com/buildtesters/buildtest/commit/fd8d466dc1f009f5822d2161eaf73e85f42a985e>`_ `9d112c <https://github.com/buildtesters/buildtest/commit/9d112c0e2e8c6800013eeda7968f568a749f2586>`_
- Fixed a bug during compiler detection when building GCC see `f1397 <https://github.com/buildtesters/buildtest/commit/f139756213a280301771214894c8f48e8bcee4e8`_
- create a pretty menu for Interactive Testing via **buildtest --runtest** see `231cfe <https://github.com/buildtesters/buildtest/commit/231cfeb0cf88cbc70826a9e76697947d06f0a6e1>`_
- replace shell commands **subprocess.Popen()** with python library equivalents
- Add support for **--testset Tcl** see `373cc1 <https://github.com/buildtesters/buildtest/commit/373cc1ea2fb2c5aedcf9ddadf105a94232cc1fa4>`_
- Add support for **--testset Ruby** see `c6b7133 <https://github.com/buildtesters/buildtest/commit/c6b7133b5fc4b0690b8040d0e437784567cc1963>`_
- Print software in alphabetical order for -svr option see `fcf610 <https://github.com/buildtesters/buildtest/commit/fcf61019c644cd305e459234a85c5d39df06433f>`_

v0.1.6 (Sep 15th, 2017)
-------------------------

- Add support for FlatNamingScheme in buildtest, added flag ``--module-naming-scheme`` to control setting
- Add prototype functions
    - get_appname()
    - get_appversion()
    - get_toolchain_name()
    - get_toolchain_version()

- Add support for logging via Python Logger module
- Fix buildtest version, in 0.1.5 release buildtest was reporting version 1.0.1
- Provide clean termination when no easyconfig is found
- Fix issue when no toolchain is provided in CMakeList.txt
- Optimize nested loop when performing --software-version-relationship

v0.1.5 (Aug 30th, 2017)
------------------------------

The buildtest repo has been moved from http://github.com/shahzebsiddiqui to http://github.com/buildtesters

- Report what tests can be generated from buildtest through YAML files by using **--scantest**
- Fixed a bug with flag **-svr** that was related to structure of easybuild repo, now no dependency on easybuild repo. Also added pretty output
- Adding CONTRIBUTION page
- Fix out software, toolchain, and easyconfig check is done. Arguments to --software and --toolchain must go through module check, then toolchain check, and then finally easyconfig check
- Add support for **--check-setup** which can be used to determine if buildtest framework is setup properly
- Add interactive testing via **buildtest --runtest** which is menu-driven with ability to run all tests, or run individual test directory in menu and see output
- Fix some issues with --testset and now buildtest reports number of tests generated not the path for each test to limit output. For --testset like R, Python, Perl buildtest will report generated test for each package
- buildtest will now use **eb --list-toolchains** to get list of all toolchains for toolchain check
- Can properly generate tests via --testset when R, Python, and Perl repos were created and moved out of buildtest-configs
- Add **buildtest -V** for version display

There has been lots of restructuring of code. There still needs some improvement for organizing scripts by functions


v0.1.4 (May 23th, 2017)
---------------------------

- Major code restructure around processing binary test and support for logging environment variable
    - BUILDTEST_LOGCONTENT
    - BUILDTEST_LOGDIR
    - BUILDTEST_LOGFILE

- Provide get functions to retrieve value from arg.parser
- Add support for Perl with ``--testset``
- Add for more logging support in module and eb verification

v0.1.3 (May 17th, 2017)
--------------------------

There have been several changes in the buildtest framework to allow for more capabilities.

The following changes have been done in this release
- buildtest can generate binary test for same executable with multiple parameters. See
- Adding support for R, Perl and Python with more tests.
- R, Python, Perl (soon to come), and MPI tests are organized in testset using **--testset** flag
this allows for multiple packages to reuse tests across different apps. For instance OpenMPI, MPICH, MVAPICH and intel can now reference the mpi testset.
- Add support for **inputfile** YAML key to allow input redirection into program.
- Add support for **outputfile** YAML key to allow output redirection.
- Add support for argument passing using **arg** key word
- Add support for **iter** YAML key to allow N tests to be created.
- Switching BUILDTEST_MODULEROOT to BUILDTEST_MODULE_EBROOT to emphasize module tree should be coming from what easybuild generates.
- Fixed some bugs pertaining to CMakeLists.txt

v0.1.2 (May 9th, 2017)
----------------------------

The current release add supports for logging by default.

buildtest will now report useful operations for each function call that can be used for troubleshooting. The logs work with options like --verbose to report extra details in log file.

- The logs display output on the following
    - Verification of software and toolchain with module file and easyconfig parameters
    - Display output of each test generated
    - Display changes to any CMakeLists.txt
    - Output key values from YAML configs
    - Output log from ancillary features like (**--list-toolchain**, **--list-unique-software**, **--software-version-relation**)

- buildtest can now search YAML configs and buildtest generated test scripts using the command **-fc** and **-ft**
- Now all buildtest-config files are removed and migrated to

v0.1.1 (May 1, 2017)
------------------------


In this release, we have restructured the source directory. Now there are two sub directories
 * ebapps
 * system

buildtest can now support binary tests for system packages. There is a command.yaml file for each system package in its own directory. Each system package is in its own subdirectory where the name of the directory is the name of the system package. buildtest is using RHEL7 package names as reference.

The following system package tests have been added

* binutils
* chrony
* git
* hwloc
* ncurses
* pinfo
* procps-ng
* sed
* time
* wget

Compile from source YAML scripts can now be stored in subdirectories. buildtest can now generate tests in sub directory, this would be essential for building tests for R, Python, Ruby, Perl, etc...

Tests for the following python packages:
 - blist
 - cryptography
 - Cython
 - dateutil
 - deap
 - funcsigs
 - mpi4py
 - netaddr
 - netifaces
 - nose
 - numpy
 - os
 - paramiko
 - paycheck
 - pytz
 - scipy
 - setuptools


Added python documentation header for each function and GPL license section in all the files

v0.1.0 (Feb 26th, 2017)
------------------------

buildtest generates test scripts from YAML files. The following apps have tests:

EasyBuild Applications
-------------------------
* Anaconda2
* binutils
* Bowtie
* Bowtie2
* CMake
* CUDA
* GCC
* git
* HDF5
* hwloc
* intel
* Java
* netCDF
* numactl
* OpenMPI
* Python

System Packages
-------------------

* acl
* coreutils
* curl
* diffstat
* gcc
* gcc-c++
* gcc-gfortran
* iptables
* ltrace
* perl
* powertop
* python
* ruby
