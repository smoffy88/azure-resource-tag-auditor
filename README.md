# Azure Resource Tag Auditor ☁️

## Overview
As cloud environments scale, maintaining strict tagging governance is critical for cost tracking, security, and operational management. This Python script automates the auditing process by authenticating securely with Microsoft Azure and identifying any Resource Groups that are missing mandatory organisational tags.

This project was built to transition manual platform administration checks into an automated, repeatable script.

## Features
* **Secure Authentication:** Utilises `AzureCliCredential` from the Azure Identity SDK to authenticate seamlessly without hardcoding any secrets.
* **Automated Extraction:** Queries the Azure Resource Management API to pull a complete list of Resource Groups and their assigned tags.
* **Compliance Auditing:** Compares current tags against a strict set of mandatory governance tags using efficient Python set operations (similar to an `EXCEPT` clause in SQL).
* **Clear Reporting:** Outputs a clean, terminal-friendly report detailing exactly which resource groups are non-compliant and the specific tags they are missing.

## Prerequisites
To run this script, you will need:
* **Python 3.x** installed on your machine.
* The **Azure CLI** installed and configured.
* An active Azure subscription where you hold at least `Reader` permissions.

## Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/smoffy88/azure-resource-tag-auditor.git

2. Install the required Python Azure SDK packages:
   ```bash
   pip install azure-identity azure-mgmt-resource

## Usage

1. Open your terminal and log into Azure:
   ```bash
   az login

* (Note: If your role requires Privileged Identity Management (PIM)) activation, ensure your role is active before running az login to secure a fresh token).

2. Open app.py and update the subscription_id variable with your target Azure Subscription ID.

3. Run the script:
   ```bash
   python app.py

## Configuration

By default, the script enforces the following mandatory tags:

* customer

* env

* market

* product

To modify the compliance rules, update the mandatory_tags set inside the main() function of app.py.