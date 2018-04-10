#!/bin/bash
OPENSTACK_DIR=${OPENSTACK_DIR:-/opt/stack}

set -x

sudo pip uninstall catsplugin -y
sudo python setup.py install
cd catsplugin
cp -rv enabled "$OPENSTACK_DIR/horizon/openstack_dashboard/local/"
