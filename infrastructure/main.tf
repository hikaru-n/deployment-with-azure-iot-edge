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
  name     = "StudyAnalyticsMTG"
  location = "japaneast"

  tags = {
    Name = "Analytics"
  }
}

# container registry
resource "azurerm_container_registry" "iot" {
  name                = "AnalyticsMTGRegistry"
  resource_group_name = azurerm_resource_group.iot.name
  location            = azurerm_resource_group.iot.location
  sku                 = "Basic"
  admin_enabled       = true
}

# azure iot hub 
resource "azurerm_iothub" "iot" {
  name                = "StudyMTGAnalyticsIoTHub"
  resource_group_name = azurerm_resource_group.iot.name
  location            = azurerm_resource_group.iot.location

  file_upload {
    default_ttl        = "PT1H"
    container_name     = ""
    connection_string  = ""
    lock_duration      = "PT1M"
    max_delivery_count = 10
    notifications      = false
    sas_ttl            = "PT1H"
  }

  sku {
    name     = "S1"
    capacity = "1"
  }
}
