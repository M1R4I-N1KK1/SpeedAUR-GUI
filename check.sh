#!/usr/bin/env bash
(gcc -c -Q -march=native --help=target | grep march | awk '{print $2}' | head -1)