#!/usr/bin/env bats

@test "provider - ad" {
  ./tfman r ad_user
}

@test "provider - alicloud" {
  ./tfman r alicloud_instance
}

@test "provider - archive" {
  ./tfman d archive_file
}

@test "provider - aws" {
  ./tfman r awscc_logs_log_group
}

@test "provider - awscc" {
  ./tfman r aws_instance
}

@test "provider - azuread" {
  ./tfman r azuread_user
}

@test "provider - azurerm" {
  ./tfman r azurerm_virtual_machine
}

@test "provider - azurestack" {
  ./tfman r azurestack_virtual_machine
}

@test "provider - boundary" {
  ./tfman r boundary_user
}

@test "provider - ciscoasa" {
  ./tfman r ciscoasa_interface_vlan
}

@test "provider - cloudflare" {
  ./tfman r cloudflare_record
}

@test "provider - cloudinit" {
  ./tfman d cloudinit_config
}

@test "provider - consul" {
  ./tfman r consul_keys
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

@test "provider - googleworkspace" {
  ./tfman r googleworkspace_user
}

@test "provider - hcp" {
  ./tfman r hcp_hvn
}

@test "provider - hcs" {
  ./tfman r hcs_cluster
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

@test "provider - libvirt" {
  ./tfman r libvirt_domain
}

@test "provider - local" {
  ./tfman r local_file
}

@test "provider - netbox" {
  ./tfman r netbox_ip_address
}

@test "provider - nomad" {
  ./tfman r nomad_job
}

@test "provider - null" {
  ./tfman r null_resource
}

@test "provider - oci" {
  ./tfman r oci_core_instance
}

@test "provider - opc" {
  ./tfman r opc_compute_instance
}

@test "provider - oraclepaas" {
  ./tfman r oraclepaas_database_service_instance
}

@test "provider - random" {
  ./tfman r random_id
}

@test "provider - salesforce" {
  ./tfman r salesforce_profile
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

@test "provider - twingate" {
  ./tfman r twingate_resource
}

@test "provider - vault" {
  ./tfman d vault_generic_secret
}

@test "provider - vsphere" {
  ./tfman r vsphere_virtual_machine
}
