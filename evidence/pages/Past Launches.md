---
title: Past Launches
hide_title: true
description: Past SpaceX Launches
---

# Past Launches

```sql pipeline_run_date
select distinct dlt_load_dttm
from motherduck.past_launches
```

Pipeline last ran on <Value data={pipeline_run_date} column = dlt_load_dttm fmt=longdate/>

```sql filters
select status,mission_type,rocket_configuration_name,pad_name
from motherduck.past_launches
```

<DimensionGrid
    multiple
    data={filters} 
    metric='count(*)'
    name=filters
    title="Filter by"
/>

```sql past_filtered
select *
from motherduck.past_launches
where ${inputs.filters}
```

<DataTable data={past_filtered} search=true>
    <Column id="image_thumbnail_url" title="Rocket Icon" contentType=image height=100px width=100px />
    <Column id=mission_name/>
    <Column id=launch_dttm_bst title="Proposed Launch Time (BST)" fmt="yyyy-mm-dd hh:mm:ss"/>
    <Column id=rocket_configuration_name title="Rocket Configuration"/>
    <Column id=mission_type />
    <Column id=pad_name />    
</DataTable>

<Note>
    Image Credits : SpaceX,NASA
</Note>