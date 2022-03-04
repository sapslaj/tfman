#!/usr/bin/env bats

@test "root - shows help" {
  # `cat` is used here as a buffer because rich/python gets upset when grep
  # closes the IO too quickly.
  ./tfman -h | cat | grep -q "Usage: tfman"
  ./tfman -h | cat | grep -q "Example: tfman"
}
