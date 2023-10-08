#!/bin/bash
echo $(dirname "$0")
COMPONENTS_DIR=$(dirname "$0")/components

bash ${COMPONENTS_DIR}/L00-disable-spectre.sh
bash ${COMPONENTS_DIR}/L01-remove-bloats.sh
bash ${COMPONENTS_DIR}/L02-network-conf.sh 1
bash ${COMPONENTS_DIR}/H00-download-hadoop.sh
bash ${COMPONENTS_DIR}/H01-setup-cluster.sh


exit