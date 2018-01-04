function savetxt(filename,data);
[m,n]=size(data);
fid=fopen(filename,'w+');
if n==1
    fprintf(fid,'%g\n',data');
else if n==2
        fprintf(fid,'%g\t%g\n',data');
    else if n==3
            fprintf(fid,'%g %g %g\n',data');
        end
    end
end
fclose(fid);
