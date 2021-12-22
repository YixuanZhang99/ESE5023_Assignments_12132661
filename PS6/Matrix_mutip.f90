subroutine Matrix_multip(m, n, res)
    implicit none

    real(8),dimension(5, 3) :: M
    real(8),dimension(3, 5) :: N
    real(8),dimension(5, 5) :: Res
    real(8)                 :: temp
    integer                 :: i, j, k

    do i = 1, 5
        do j = 1, 5
            temp = 0.
            do k = 1, 3
                temp = temp + (m(i, k) * n(k, j))
            enddo
            res(i,j) = temp
        enddo
    enddo

end subroutine Matrix_multip