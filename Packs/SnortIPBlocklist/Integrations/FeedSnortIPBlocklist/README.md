Use the Snort IP Block List feed integration to fetch IP indicators from [Snort](https://snort.org/).

## Configure Snort IP Blocklist in Cortex

| **Parameter** | **Description** | **Required** |
| --- | --- | --- |
| Fetch indicators |  | False |
| Server's URL | Should be feed of type .txt. For using other types of feed, modify the parsing in the python file. | True |
| Indicator Reputation | Indicators from this integration instance will be marked with this reputation | False |
| Source Reliability | Reliability of the source providing the intelligence data | True |
| Traffic Light Protocol Color | The Traffic Light Protocol \(TLP\) designation to apply to indicators fetched from the feed | False |
| Feed Fetch Interval |  | False |
| Bypass exclusion list | When selected, the exclusion list is ignored for indicators from this feed. This means that if an indicator from this feed is on the exclusion list, the indicator might still be added to the system. | False |
| Trust any certificate (not secure) |  | False |
| Use system proxy settings |  | False |
| Tags | Supports CSV values. | False |

## Commands

You can execute these commands from the CLI, as part of an automation, or in a playbook.
After you successfully execute a command, a DBot message appears in the War Room with the command details.

### snort-get-ip-blocklist-indicators

***
Gets indicators from the feed.

#### Base Command

`snort-get-ip-blocklist-indicators`

#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| limit | The maximum number of results to return. Default is 10. | Optional |

#### Context Output

There is no context output for this command.
