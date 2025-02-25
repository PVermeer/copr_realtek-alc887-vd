#!/bin/bash

set -e
set -x

rm -rf ./rpmbuild
mkdir -p ./rpmbuild/SOURCES

rpmlint ./hdajackretask-realtek-alc887-vd.spec
rpmbuild --define "_topdir $PWD/rpmbuild" -ba --noclean ./hdajackretask-realtek-alc887-vd.spec
rpm -qvlp ./rpmbuild/RPMS/**/*.rpm
rpm -qp --scripts ./rpmbuild/RPMS/**/*.rpm
