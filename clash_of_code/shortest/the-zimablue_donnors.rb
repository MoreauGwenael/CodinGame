n,*l,d=$<.map &:split
a,*b=l.select{_2==d[0]}.sort_by{(d[1].to_i-_3.to_i).abs}.map{_1[0]}
puts n[0]>?0?a.nil?? "NO COMPATIBLE DONOR":"MOST COMPATIBLE DONOR : #{a}#{b[0]?"
OTHER COMPATIBLE DONORS :
#{b*"\n"}":""}":"NO DONOR AVAILABLE"
