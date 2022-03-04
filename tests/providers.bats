#!/usr/bin/env bats

@test "provider - ad" {
  ./tfman r ad_user
}

@test "provider - alicloud" {
  ./tfman r alicloud_instance
}

@test "provider - aws" {
  ./tfman r aws_instance
}

@test "provider - azurerm" {
  ./tfman r azurerm_virtual_machine
}

@test "provider - cloudinit" {
  ./tfman d cloudinit_config
}

@test "provider - datadog" {
  ./tfman r datadog_user
}

@test "provider - dns" {
  ./tfman r dns_a_record_set
}

@test "provider - external" {
  ./tfman d external
}

@test "provider - github" {
  ./tfman r github_repository
}

@test "provider - google" {
  ./tfman r google_compute_instance
}

@test "provider - helm" {
  ./tfman r helm_release
}

@test "provider - http" {
  ./tfman d http
}

@test "provider - kubernetes" {
  ./tfman r kubernetes_deployment
}

@test "provider - lacework" {
  ./tfman r lacework_policy
}

@test "provider - local" {
  ./tfman r local_file
}

@test "provider - netbox" {
  ./tfman r netbox_ip_address
}

@test "provider - null" {
  ./tfman r null_resource
}

@test "provider - oci" {
  ./tfman r oci_core_instance
}

@test "provider - random" {
  ./tfman r random_id
}

@test "provider - tfe" {
  ./tfman r tfe_workspace
}

@test "provider - time" {
  ./tfman r time_rotating
}

@test "provider - tls" {
  ./tfman d tls_public_key
}

@test "provider - vault" {
  ./tfman d vault_generic_secret
}
