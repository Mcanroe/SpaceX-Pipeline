{% macro is_in_past(column_name) %}
  {% set current_timestamp_bst = dbt.current_timestamp() ~ " at time zone 'Europe/London'" %}
  {{ column_name }} < {{ current_timestamp_bst }}
  AND {{ column_name }} IS NOT NULL
{% endmacro %}