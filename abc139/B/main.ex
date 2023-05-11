defmodule Main do

    def solve(a,b) do
        ans = Float.ceil(a/b)
        IO.puts(ans)
    end

    def main() do
        a,b =
            IO.read(:line)
            |> String.split(" ")
            |> Enum.map(String.to_integer)
        solve(a,b)
    end
end
