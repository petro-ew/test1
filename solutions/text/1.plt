set term png 
set output "plot.png"
set xtics 1
plot [] [0:] "./plan.txt" using 1:2 with lines title "aaa", "./plan.txt" using 1:3 with lines title "bbb", "./plan.txt" using 1:4 with lines title "ccc"

