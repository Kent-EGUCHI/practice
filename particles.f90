!-----------------------------------------------------------------------------
module particles
!-----------------------------------------------------------------------------
  use cylinder
  implicit none
  integer, parameter :: NPmax=1000000
  integer :: IPmax
  real(kind=8) :: Xp(NPmax),Yp(NPmax)
  contains
!-----------------------------------------------------------------------------
  subroutine particles_add
!-----------------------------------------------------------------------------
  integer :: i
  if (IPmax+3.gt.NPmax) then
     write(*,*) 'too much'
     return
  end if
  do i=0,2
     XP(IPmax+i+1)=1.2d0*(D/2.d0)*cos(-0.1d0+real(i,8)*0.1d0)
     YP(IPmax+i+1)=1.2d0*(D/2.d0)*sin(-0.1d0+real(i,8)*0.1d0)
  end do
  XP(IPmax+4)=0.0
  YP(IPmax+4)=1.2d0*(D/2.d0)
  XP(IPmax+5)=0.0
  YP(IPmax+5)=-1.2d0*(D/2.d0)
  IPmax=IPmax+5
  end subroutine particles_add
!-----------------------------------------------------------------------------
  subroutine particles_move(Vx,Vy)
!-----------------------------------------------------------------------------
  real(kind=8) :: Vx(NXmin:NXmax,NYmin:NYmax)
  real(kind=8) :: Vy(NXmin:NXmax,NYmin:NYmax)
  integer :: IP,iX,iY
  integer :: JP
  JP=0
  do IP=1,IPmax
     iX=int(Xp(IP)/dX)
     iY=int(Yp(IP)/dX)
     if (iX.lt.NXmax.and.iY.gt.NYmin.and.iY.lt.NYmax) then
        JP=JP+1
        Xp(JP)=Xp(IP)+Vx(iX,iY)*dt
        Yp(JP)=Yp(IP)+Vy(iX,iY)*dt
     end if
  end do
  IPmax=JP
  end subroutine particles_move
!-----------------------------------------------------------------------------
  subroutine particles_out(istep)
!-----------------------------------------------------------------------------
  integer :: IP
  integer :: istep
  character(6) :: cistep
  write(cistep,'(i6.6)') istep
  open(20,file='./data/particle.'//cistep)
  do IP=1,IPmax
     write(20,'(2e14.6)') Xp(IP),Yp(IP)
  end do
  close(20)
  end subroutine particles_out
end module particles
