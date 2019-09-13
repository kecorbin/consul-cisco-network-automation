provider "aci" {
  # credentials
  url      = var.aci_url
  username = var.aci_username
  password = var.aci_password
  insecure = true
  // proxy_url = "https://proxy_server:proxy_port"
}


resource "aci_tenant" "HashiCorp" {
  name        = "HashiCorp-${var.environment}"
  description = "This tenant is created by terraform"
}

resource "aci_application_profile" "app1" {
  tenant_dn   = "${aci_tenant.HashiCorp.id}"
  name        = "app1"
  description = "This app profile is created by terraform"
}

resource "aci_application_epg" "app1" {
   application_profile_dn  = "${aci_application_profile.app1.id}"
   name                            = "app1"
   description                   = "this epg is created by terraform"
   annotation                    = "tag_epg"
}
resource "aci_l3_outside" "outside_network" {
    tenant_dn      = "${aci_tenant.HashiCorp.id}"
    description    = "Rename"
    name           = "consul_services"
    annotation     = "tag_l3out"
    name_alias     = "outside_network"
    target_dscp    = "unspecified"
}

resource "aci_external_network_instance_profile" "demo_inst_prof" {
    l3_outside_dn  = "${aci_l3_outside.outside_network.id}"
    description    = "TODO: RENAME"
    name           = "demo_inst_prof"
    annotation     = "tag_network_profile"
    exception_tag  = "2"
    flood_on_encap = "disabled"
    name_alias     = "alias_profile"
    prio           = "level1"

}
