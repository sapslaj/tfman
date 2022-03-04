#!/usr/bin/env bats

@test "platform - expressions" {
  ./tfman e types
}

@test "platform - functions" {
  ./tfman f file
}

@test "platform - meta-arguments" {
  ./tfman m for_each
}
