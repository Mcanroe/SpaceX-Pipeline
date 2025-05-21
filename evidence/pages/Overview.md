---
title: Overview
hide_title: true
description: Dashboard Overview
sidebar_position: 1
---

# Overview

```sql pipeline_run_date
select distinct dlt_load_dttm
from motherduck.past_launches
```

Pipeline last ran on <Value data={pipeline_run_date} column = dlt_load_dttm fmt=longdate/>

<Alert status="warning">
The following visualizations are based on historical launch data. Upcoming launch data is excluded as it frequently changes and can have placeholder data.
</Alert>

```sql pie_chart
select status as name,count(*) as value
from motherduck.past_launches
group by status
```

<ECharts config={
    {
        tooltip: {
            formatter: '{b}: {c} ({d}%)'
        },
        title : {
            text: 'Launch Results',
        },
        series: [
        {
          type: 'pie',
          data: [...pie_chart],
        }
      ]
      }
    }
/>

```sql bar_chart
select year(launch_dttm_bst)::varchar as launch_year,count(*) as launches
from motherduck.past_launches 
group by year(launch_dttm_bst)
order by year(launch_dttm_bst) desc
```

<BarChart 
    data={bar_chart}
    title="Launches by Year"
    legend=true
    showAllLabels=true
    x=launch_year
    xAxisTitle="Year"
    y=launches
    labels=true
    sort=false
/>

```sql pad_launches
select *
from motherduck.pad_overview
```

<DataTable data={pad_launches} sort="pad_total_launch_count desc" title="Launches by Pad">
    <Column id=pad_name/>
    <Column id=pad_total_launch_count title="Total Launches"/>
    <Column id=pad_wiki_url contentType=link linkLabel="Details" title="Wikipedia URL" openInNewTab=true/>
    <Column id="pad_map_image" title="Pad Map Image" contentType=image height=300px width=500px />
</DataTable>