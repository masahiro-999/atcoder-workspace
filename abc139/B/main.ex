defmodule Main do

    def get_ans(num_tap, socket, a, b) do
        cond do
         socket >= b -> num_tap
         num_tap == 0 -> get_ans(1, a, a, b)
         :true -> get_ans(num_tap+1, socket+a-1, a, b)
        end
    end
    def solve(a,b) do
        ans = get_ans(0, 1, a, b)
        IO.puts(ans)
    end

    def main() do
        [a,b] = IO.read(:line)
            |> String.trim()
            |> String.split(" ")
            |> Enum.map(&String.to_integer/1)
        solve(a,b)
    end
end
