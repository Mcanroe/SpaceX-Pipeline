---
title: Upcoming Launches
hide_title: true
description: Upcoming SpaceX launches
sidebar_position: 1
---

# Upcoming Launches

```sql upcoming
select *
from motherduck.upcoming_launches
```

Pipeline last ran on <Value data={upcoming} column = dlt_load_dttm fmt=longdate/>

<DataTable data={upcoming} search=true>
    <Column id="image_thumbnail_url" title="Rocket Icon" contentType=image height=100px width=100px />
    <Column id=mission_name/>
    <Column id=launch_dttm_bst title="Proposed Launch Time (BST)" fmt="yyyy-mm-dd hh:mm:ss"/>
    <Column id=rocket_configuration_name title="Rocket Configuration"/>
    <Column id=mission_type />
    <Column id=pad_name />    
</DataTable>

<Note>
    Image Credits : SpaceX
</Note>