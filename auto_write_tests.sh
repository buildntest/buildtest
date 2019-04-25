#!/bin/bash
script_dir="./docs/scripts"
tee $script_dir/buildtest-help.txt <<<"buildtest --help" | bash >> $script_dir/buildtest-help.txt

# Show Subcommand
tee $script_dir/buildtest-show-help.txt <<<"buildtest show --help" | bash >> $script_dir/buildtest-show-help.txt
tee $script_dir/buildtest-show-configuration.txt <<<"buildtest show -c" | bash >> $script_dir/buildtest-show-configuration.txt
tee $script_dir/buildtest-show-key.txt <<<"buildtest show -k singlesource" | bash >> $script_dir/buildtest-show-key.txt

# build Subcommand
tee $script_dir/buildtest-build-help.txt <<<"buildtest build --help" | bash >> $script_dir/buildtest-build-help.txt
tee $script_dir/custom-testdir.txt <<< "buildtest build --package gcc --testdir $HOME/tmp" | bash >> $script_dir/custom-testdir.txt
tee $script_dir/coreutils-binary-test.txt <<<"buildtest build --package coreutils" | bash >> $script_dir/coreutils-binary-test.txt

tee $script_dir/build-compilers-suite.txt <<<"buildtest build -S compilers" |bash>> $script_dir/build-compilers-suite.txt
tee $script_dir/run-compilers-suite.txt <<<"buildtest run -S compilers"|bash>> $script_dir/run-compilers-suite.txt

tee $script_dir/build-openmp-suite.txt <<<"buildtest build -S openmp" |bash>>$script_dir/build-openmp-suite.txt
tee $script_dir/run-openmp-suite.txt <<<"buildtest run -S openmp"| bash>>$script_dir/run-openmp-suite.txt


tee $script_dir/build-single-configuration.txt <<<"buildtest build -c $BUILDTEST_ROOT/toolkit/buildtest/suite/compilers/helloworld/hello_gnu.yml -vv" | bash >>$script_dir/build-single-configuration.txt

tee $script_dir/build-single-configuration-module.txt <<<"ml eb/2018; ml GCC; buildtest build -c $BUILDTEST_ROOT/toolkit/buildtest/suite/compilers/helloworld/hello_gnu.yml -vv" | bash >>$script_dir/build-single-configuration-module.txt

tee $script_dir/build-shell-csh.txt <<<"buildtest build -c $BUILDTEST_ROOT/toolkit/buildtest/suite/compilers/helloworld/hello_gnu.yml --shell csh" | bash >>$script_dir/build-shell-csh.txt
tee $script_dir/build-shell-bash.txt <<<"BUILDTEST_SHELL=bash buildtest build -c $BUILDTEST_ROOT/toolkit/buildtest/suite/compilers/helloworld/hello_gnu.yml" | bash >>$script_dir/build-shell-bash.txt

# lsf example
tee $script_dir/build-lsf-example.txt <<<"buildtest build -c $BUILDTEST_ROOT/toolkit/buildtest/suite/compilers/helloworld/hello_lsf.yml -vv""" | bash >>$script_dir/build-lsf-example.txt
# slurm example
tee $script_dir/build-slurm-example.txt <<<"buildtest build -c $BUILDTEST_ROOT/toolkit/buildtest/suite/compilers/helloworld/hello_slurm.yml -vv""" | bash >>$script_dir/build-slurm-example.txt

# List Subcommand
tee $script_dir/buildtest-list-help.txt <<<"buildtest list --help" | bash >> $script_dir/buildtest-list-help.txt
tee $script_dir/buildtest-list-software.txt <<< "buildtest list -ls" | bash >> $script_dir/buildtest-list-software.txt
tee $script_dir/buildtest-list-software-modules.txt <<< "buildtest list -svr" | bash >> $script_dir/buildtest-list-software-modules.txt
tee $script_dir/buildtest-list-easyconfigs.txt <<< "buildtest list --easyconfigs" | bash >> $script_dir/buildtest-list-easyconfigs.txt
tee $script_dir/buildtest-list-software-format.txt <<< "buildtest list -ls --format=json" | bash >> $script_dir/buildtest-list-software-format.txt

# Find Subcommand
tee $script_dir/buildtest-find-help.txt <<<"buildtest find --help" | bash >> $script_dir/buildtest-find-help.txt
tee $script_dir/buildtest-find-configs.txt <<<"buildtest find -fc all" | bash >> $script_dir/buildtest-find-configs.txt
tee $script_dir/buildtest-find-test.txt <<<"buildtest find -ft all" | bash >> $script_dir/buildtest-find-test.txt

# module load test
tee $script_dir/module-load.txt <<<"buildtest module --module-load-test" | bash >> $script_dir/module-load.txt
tee $script_dir/module-diff.txt <<<"buildtest module --diff-trees /clust/app/easybuild/2018/commons/modules/all,/usr/share/lmod/lmod/modulefiles/Core" | bash >> $script_dir/module-diff.txt
tee $script_dir/module-diff-v2.txt <<< "buildtest module --diff-trees /clust/app/easybuild/2018/Broadwell/redhat/7.3/modules/all,/clust/app/easybuild/2018/IvyBridge/redhat/7.3/modules/all" | bash >> $script_dir/module-diff-v2.txt
