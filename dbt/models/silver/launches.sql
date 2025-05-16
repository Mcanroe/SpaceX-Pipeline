{{ config(materialized='table') }}

select 
    id as launch_id,
    "name",
    launch_designator,
    status__id as status_id,
    status__abbrev as "status",
	status__description as "description",
    net at time zone 'Europe/London' as launch_dttm_bst, -- convert UTC to BST
    image__thumbnail_url as image_thumbnail_url,
    image__credit as image_credit,
    failreason as fail_reason,
    rocket__id as rocket_id,
    rocket__configuration__full_name as rocket_configuration_name,
    mission__id as mission_id,
    mission__name as mission_name,
    mission__type as mission_type,
    mission__description as mission_description,
    mission__orbit__id as mission_orbit_id,
    mission__orbit__name as mission_orbit_name,
    pad__id as pad_id,
    pad__name as pad_name,
    last_updated at time zone 'Europe/London' as last_updated_bst,
    _dlt_load_id as dlt_load_id,
    dlt.inserted_at at time zone 'Europe/London' as dlt_load_dttm
from {{ source('bronze', 'launches') }} lch
inner join {{ source('bronze', '_dlt_loads') }} dlt
on lch._dlt_load_id = dlt.load_id