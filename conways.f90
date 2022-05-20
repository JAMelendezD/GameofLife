! ------------------------------------------------------------------------------
!  conways.f90 : Conways game of life in Fortran (39.83)
! ------------------------------------------------------------------------------

module tools
  implicit none
  contains

  subroutine update_world(rows, cols, world)

    integer, intent (inout) :: world(:, :)
    integer, allocatable :: old_world(:, :)
    integer :: i, j, state, neis, rows, cols
    old_world = world
  
    do i = 1, rows
      do j = 1, cols
        state = old_world(i,j)
        neis = old_world(mod(i - 1, rows) + 1, mod(j, cols) + 1) &
              +old_world(mod(i - 1, rows) + 1, mod(j - 2, cols) + 1) &
              +old_world(mod(i, rows) + 1, mod(j - 1, cols) + 1) &
              +old_world(mod(i - 2, rows) + 1, mod(j - 1, cols) + 1) &
              +old_world(mod(i, rows) + 1, mod(j, cols) + 1) &
              +old_world(mod(i - 2, rows) + 1, mod(j - 2, cols) + 1) &
              +old_world(mod(i, rows) + 1, mod(j - 2, cols) + 1) &
              +old_world(mod(i - 2, rows) + 1, mod(j, cols) + 1)

        if (state == 1) then
          if (neis /= 2 .AND. neis /= 3) then
            world(i,j) = 0
          end if
        else
          if (neis == 3) then
            world(i,j) = 1
          end if
        end if 
      end do
    end do
    deallocate(old_world)
  end subroutine update_world

  subroutine write_file(name, rows, cols, world)

    integer, intent(in) :: world(:,:)
    character(len=1024) :: name
    integer :: rows, cols
    integer :: i, j
    
    open (unit = 999, file = name)
    do i = 1, rows
      do j = 1, cols
        write(999, '(A, I1)', advance = 'no') ' ', world(i,j)
      end do
      write(999, '(A)')
    end do
    close(999) 
  end subroutine write_file
end module tools

program main
  use tools

  integer :: rows, cols, frame, frames
  character(12) :: arg1, arg2, arg3
  real :: startTime, stopTime
  character(len=1024) :: name
  real, allocatable :: tmp_arr(:, :)
  integer, allocatable :: world(:, :)

  call get_command_argument(1, arg1)
  call get_command_argument(2, arg2)
  call get_command_argument(3, arg3)

  read(arg1, *)rows
  read(arg2, *)cols
  read(arg3, *)frames
  
  allocate(tmp_arr(rows, cols))
  allocate(world(rows, cols))

  call random_number(tmp_arr)
  world = floor(2 * tmp_arr)
  deallocate(tmp_arr)
  
  write(*, '(A)') 'Started simulation'
  call cpu_time(startTime)
  do frame = 1, frames
    write(name, '(I0.6, A)') frame, '.txt'
    call write_file(name, rows, cols, world)
    call update_world(rows, cols, world)
  end do
  call cpu_time(stopTime)
  write(*, '(A, F6.2, A)') 'Finished simulation in: ', &  
          (stopTime - startTime), ' seconds'
  deallocate(world)
end program