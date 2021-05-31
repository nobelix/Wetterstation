#!/usr/bin/gnuplot
#Gnuplot script
set datafile separator ";"
set timefmt "%d.%m.%Y %H:%M:%S"
set xdata time            
set format x "%H:%M"
set autoscale
set term x11 size 800,425 

set terminal x11 0 title "Luftdruck" noraise
	 set title "Luftdruck"
	 set ylabel "mbar"
	 set xlabel "Zeit"
	 set grid
	 show grid
	 plot "wetter.dat" using 1:2 title 'Luftdruck' with lines smooth sbezier

set terminal x11 1 title "Luftfeuchtigkeit" noraise
	 set title "Luftfeuchtigkeit"
	 set ylabel "%"
	 set xlabel "Zeit"
	 plot "wetter.dat" using 1:5 title 'Luftfeuchtigkeit' with lines smooth sbezier

set terminal x11 2 title "Temperatur" noraise
	 set title "Temperatur"
	 set ylabel "°C"
	 set xlabel "Zeit"
	 plot "wetter.dat" using 1:3 title 'Lufttemperatur' with lines smooth sbezier, "wetter.dat" using 1:4 title 'Bodentemperatur' with lines smooth sbezier


pause 10
reread
