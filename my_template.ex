defmodule Main do

{% if mod %}
    MOD = {{ mod }}
{% endif %}
{% if yes_str %}
    YES = "{{ yes_str }}"
{% endif %}
{% if no_str %}
    NO = "{{ no_str }}"
{% endif %}

{% if prediction_success %}
    def solve({{ formal_arguments }}) do

    end
{% endif %}

    def main() do
    {% if prediction_success %}
        {{input_part}}
        solve({ actual_arguments })
    {% else %}
        # Failed to predict input format
    {% endif %}


