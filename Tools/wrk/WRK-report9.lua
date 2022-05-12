done = function(summary, latency, requests)

    f = io.open("wrk9.csv", "w")

    for i = 0, summary.requests - 1 do
        f:write(latency(i))
        f:write("\n")
    end

    f:close()
end