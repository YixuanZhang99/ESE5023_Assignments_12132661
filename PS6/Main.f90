program Main

implicit none

integer                 :: u, i , j
real(8),dimension(5, 3) :: M
real(8),dimension(3, 5) :: N
real(8),dimension(5, 5) :: Res


u = 50
open(unit = u, file = 'M.dat', status = 'old')
do i=1, 5
read(u,*) M(i,1), M(i,2), M(i,3)
enddo
close(u)

u = 55
open(unit = u, file = 'N.dat', status = 'old')
do i = 1, 3
read(u,*) N(i,1), N(i,2), N(i,3), N(i,4), N(i,5)
enddo
close(u)

call Matrix_multip(M, N, Res)

u = 65
open(unit = u, file = 'MN.dat', status = 'replace')
do i = 1,5
    write(u,'(f9.2, f9.2, f9.2, f9.2, f9.2)') Res(i,1), Res(i,2), Res(i,3), Res(i,4), Res(i,5)
enddo

end program Main