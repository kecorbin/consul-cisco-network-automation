#!/bin/bash
consul agent -retry-join consul3 -client 0.0.0.0 &
consul watch -type=service -service=web /updater/update.py
