module test_module
    implicit none
    integer :: a =1
    integer :: b = 4
contains
    subroutine add_1
    implicit none
    a = a+1
    
    end subroutine add_1

    subroutine devide
    implicit none
    b = b/a
    end subroutine devide
end module test_module

program test
    use test_module
    implicit none

    character(len=100) :: greet = "Hello!"

    !write(*,*) "before call add a=",a
    !call add_1
    !write(*,*) "after call add a=",a

    !write(*,*) "before call devide b=",b
    !call devide
    !write(*,*) "after call devide a=",b

    print *,trim(greet)

    write(greet,*) 4649

    print *,adjustl(greet)

end program test