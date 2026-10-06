#!/usr/bin/env bash
#
# Minimal public call example for ST21-Door.
#
# Usage:
#   ST21_TRIAL_HEADER='<trial header line issued to you>' ./examples/check.sh
#
# The trial header name and value are issued separately.  They are kept private
# on the server side and are deliberately NOT published in this repository.
#
set -euo pipefail

ENDPOINT="${ST21_DOOR_ENDPOINT:-https://shishuanglu21.com/door/check}"
BODY="$(dirname "$0")/check-request.json"
: "${ST21_TRIAL_HEADER:?set ST21_TRIAL_HEADER to the trial header issued to you, in the form 'Name: value'}"

curl -sS -m 300 \
  -X POST "$ENDPOINT" \
  -H 'Content-Type: application/json' \
  -H "$ST21_TRIAL_HEADER" \
  --data @"$BODY" \
  -w '\nHTTP_STATUS=%{http_code}\n'
