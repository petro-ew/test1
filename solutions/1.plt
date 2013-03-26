set term png 
set output "plot-histeps.png"
set xtics 1
plot [] [0:] "./plan.txt" using 1:2 with histeps title "slips < 10", "./plan.txt" using 1:3 with histeps title "slips > 10", "./plan.txt" using 1:4 with histeps title "MP < 10", "./plan.txt" using 1:5 with histeps title "MP > 10"
set term png
set output "plot-lines.png"
set xtics 1
plot [] [0:] "./plan.txt" using 1:2 with lines title "slips < 10", "./plan.txt" using 1:3 with lines title "slips > 10", "./plan.txt" using 1:4 with lines title "MP < 10", "./plan.txt" using 1:5 with lines title "MP > 10"

