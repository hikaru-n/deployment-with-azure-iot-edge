terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "=2.46.0"
    }
  }
}


provider "azurerm" {
  features {}
}

# resource group
resource "azurerm_resource_group" "iot" {
  name     = var.resource_group_name
  location = var.location

}

# container registry
resource "azurerm_container_registry" "iot" {
  name                = var.container_registry_name
  resource_group_name = var.resource_group_name
  location            = var.location
  sku                 = "Basic"
  admin_enabled       = true
}

# azure iot hub 
resource "azurerm_iothub" "iot" {
  name                = var.iothub_name
  resource_group_name = var.resource_group_name
  location            = var.location

  fallback_route {
    source = "DeviceMessages"
    condition = true
    endpoint_names  = ["events"]
    enabled = true
  }

  sku {
    name     = "S1"
    capacity = "1"
  }
}
