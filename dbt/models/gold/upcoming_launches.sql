select * 
from {{ ref('launches') }}
where status_id not in (3,4) -- all events that are not success or failure , includes events that are TBC, TBD , etc.