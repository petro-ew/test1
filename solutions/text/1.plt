set term png 
set output "plot.png"
set xtics 1
plot [] [0:] "./plan.txt" using 1:2 with lines title "slips < 10", "./plan.txt" using 1:3 with lines title "slips > 10", "./plan.txt" using 1:4 with lines title "MP < 10", "./plan.txt" using 1:5 with lines title "MP > 10"

