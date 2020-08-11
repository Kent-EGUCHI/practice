!-----------------------------------------------------------------------------
!
! 総合演習 2019 円柱後流のプログラム（ver.6.5） M. Otsuki (2018/12/03)
!
! ** 粒子モジュールなし／オイラー ** 【配布用：穴埋あり】
!
!-----------------------------------------------------------------------------
module cylinder
  integer(kind=4), parameter :: NXmin=-16,NXmax=128 ! 計算領域の形状
  integer(kind=4), parameter :: NYmin=-32,NYmax=32  ! 計算領域の形状
  real(kind=8), parameter :: Xmax=12.d0             ! 計算領域の大きさ
  real(kind=8), parameter :: D=2.d0                 ! 円柱の直径
  real(kind=8), parameter :: U=1.d0                 ! 流入速度
  real(kind=8), parameter :: NU=0.04d0              ! 動粘性係数
  real(kind=8), parameter :: dt=0.01d0              ! 時間刻み
  integer(kind=4), parameter :: Nstep=60000         ! トータルステップ数
  integer(kind=4), parameter :: iout=1000           ! 出力間隔
  integer(kind=4), parameter :: iSep=2              ! 出力データの間引き
  real(kind=8) :: Xmin,dX
  real(kind=8) :: Ymax,Ymin
  integer(kind=4) :: iX1(NYmin:NYmax),iX2(NYmin:NYmax)
  integer(kind=4) :: iY1(NXmin:NXmax),iY2(NXmin:NXmax)
  integer(kind=4) :: iXb1,iXb2
  integer(kind=4) :: istep
  contains
!-----------------------------------------------------------------------------
  subroutine cal_rhs(Vx,Vy,P,Rx,Ry)
!-----------------------------------------------------------------------------
! ■ 運動方程式の右辺の計算
!-----------------------------------------------------------------------------
  real(kind=8) :: Vx(NXmin:NXmax,NYmin:NYmax)
  real(kind=8) :: Vy(NXmin:NXmax,NYmin:NYmax)
  real(kind=8) :: P (NXmin:NXmax,NYmin:NYmax)
  real(kind=8) :: Rx(NXmin:NXmax,NYmin:NYmax)
  real(kind=8) :: Ry(NXmin:NXmax,NYmin:NYmax)
  real(kind=8) :: C1,C2
  C1=1.d0/(2.d0*dX)
  C2=1.d0/(dX**2)
  Rx(:,:)=0.d0
  Ry(:,:)=0.d0
  do iX=NXmin+1,NXmax-1
  do iY=NYmin+1,NYmax-1
     Rx(iX,iY)=-Vx(iX,iY)*C1*(Vx(iX+1,iY)-Vx(iX-1,iY))&
		-Vy(iX,iY)*C1*(Vx(iX,iY+1)-Vx(iX,iY-1))&
		-C1*(P(iX+1,iY)-P(iX-1,iY))&
		+NU*C2*(Vx(iX+1,iY)-2*Vx(iX,iY)+Vx(iX-1,iY))&
		+NU*C2*(Vx(iX,iY+1)-2*Vx(iX,iY)+Vx(iX,iY-1))
               
               
     Ry(iX,iY)=-Vx(iX,iY)*C1*(Vy(iX+1,iY)-Vy(iX-1,iY))&
		-Vy(iX,iY)*C1*(Vy(iX,iY+1)-Vy(iX,iY-1))&
		-C1*(P(iX,iY+1)-P(iX,iY-1))&
		+NU*C2*(Vy(iX+1,iY)-2*Vy(iX,iY)+Vy(iX-1,iY))&
		+NU*C2*(Vy(iX,iY+1)-2*Vy(iX,iY)+Vy(iX,iY-1))
               
               
               

  enddo
  enddo
  end subroutine cal_rhs
!-----------------------------------------------------------------------------
  subroutine ibm(Vx,Vy,Rx,Ry)
!-----------------------------------------------------------------------------
! ■ 埋め込み境界法
!-----------------------------------------------------------------------------
  real(kind=8) :: Vx(NXmin:NXmax,NYmin:NYmax)
  real(kind=8) :: Vy(NXmin:NXmax,NYmin:NYmax)
  real(kind=8) :: Rx(NXmin:NXmax,NYmin:NYmax)
  real(kind=8) :: Ry(NXmin:NXmax,NYmin:NYmax)
  do iX=iXb1,iXb2
  do iY=iY1(iX),iY2(iX)
     Rx(iX,iY)=Rx(iX,iY)-Vx(iX,iY)/dt
     Ry(iX,iY)=Ry(iX,iY)-Vy(iX,iY)/dt
  enddo
  enddo
  end subroutine ibm
!-----------------------------------------------------------------------------
  subroutine march(Vx,Vy,P)
!-----------------------------------------------------------------------------
! ■ 時間発展
!-----------------------------------------------------------------------------
  real(kind=8) :: Vx(NXmin:NXmax,NYmin:NYmax)
  real(kind=8) :: Vy(NXmin:NXmax,NYmin:NYmax)
  real(kind=8) :: P (NXmin:NXmax,NYmin:NYmax)
  real(kind=8) :: Rx(NXmin:NXmax,NYmin:NYmax)
  real(kind=8) :: Ry(NXmin:NXmax,NYmin:NYmax)
!
  call cal_rhs(Vx,Vy,P,Rx,Ry)
  call ibm(Vx,Vy,Rx,Ry)
!
  Vx(:,:)=Vx(:,:)+Rx(:,:)*dt
  Vy(:,:)=Vy(:,:)+Ry(:,:)*dt
!
  call poisson(Vx,Vy,P)
  end subroutine march
!-----------------------------------------------------------------------------
  subroutine poisson(Vx,Vy,P)
!-----------------------------------------------------------------------------
! ■ 圧力についての Poisson 方程式
!-----------------------------------------------------------------------------
  real(kind=8) :: Vx(NXmin:NXmax,NYmin:NYmax)
  real(kind=8) :: Vy(NXmin:NXmax,NYmin:NYmax)
  real(kind=8) :: P (NXmin:NXmax,NYmin:NYmax)
  real(kind=8) :: P2(NXmin:NXmax,NYmin:NYmax)
  real(kind=8) :: NLx(NXmin:NXmax,NYmin:NYmax)
  real(kind=8) :: NLy(NXmin:NXmax,NYmin:NYmax)
  real(kind=8) :: RHS(NXmin:NXmax,NYmin:NYmax)
  real(kind=8) :: C1,C2,C13,CRedX
  real(kind=8) :: alpha
  real(kind=8) :: delta
  real(kind=8) :: divU,divN
  integer(kind=4), parameter :: itrmax=10000
  real(kind=8), parameter :: eps=1.d-2  
  C1=1.d0/(2.d0*dX)
  C2=dX**2
  C13=1.d0/3.d0
  CRedX=2.d0/(Re*dX)
  alpha=0.5d0
  do iX=NXmin+1,NXmax-1
  do iY=NYmin+1,NYmax-1
     NLx(iX,iY)=Vx(iX,iY)*C1*(Vx(iX+1,iY)-Vx(iX-1,iY)) &
               +Vy(iX,iY)*C1*(Vx(iX,iY+1)-Vx(iX,iY-1))                 
     NLy(iX,iY)=Vx(iX,iY)*C1*(Vy(iX+1,iY)-Vy(iX-1,iY)) &
               +Vy(iX,iY)*C1*(Vy(iX,iY+1)-Vy(iX,iY-1))                 
  enddo
  enddo
  do iX=NXmin+1,NXmax-1
  do iY=NYmin+1,NYmax-1
     divN=-C1*(NLx(iX+1,iY)-NLx(iX-1,iY)) &
          -C1*(NLy(iX,iY+1)-NLy(iX,iY-1)) 
     divU=C1*(Vx(iX+1,iY)-Vx(iX-1,iY)+Vy(iX,iY+1)-Vy(iX,iY-1))
     RHS(iX,iY)=divN !+divU/dt
  enddo
  enddo

 if (mod(istep,10).eq.0) then
    iX=NXmax/4
    iY=0
    write(*,*) 'divU = ',C1*(Vx(iX+1,iY)-Vx(iX-1,iY)+Vy(iX,iY+1)-Vy(iX,iY-1))
 end if

  do iterate=1,itrmax
     P2(:,:)=0.d0
     do iX=NXmin+1,NXmax-1
     do iY=NYmin+1,NYmax-1
        P2(iX,iY)=0.25d0*(P(iX-1,iY)+P(iX+1,iY)+P(iX,iY-1)+P(iX,iY+1)) &
                 -C2*0.25*RHS(iX,iY)
     enddo
     enddo
     delta=0.d0
     do iX=NXmin+1,NXmax-1
     do iY=NYmin+1,NYmax-1
        delta=max(delta,dabs(P2(iX,iY)-P(iX,iY)))
     enddo
     enddo
     P(:,:)=P(:,:)+alpha*(P2(:,:)-P(:,:))
     if (delta < eps) goto 1
  end do
  write(*,'(a,i8)') '**** poission solver did not converge at istep = ',istep
  stop 
1 continue
! write(*,'(a,i6)') 'possison solver converged: iteration = ',iterate
  end subroutine poisson
!-----------------------------------------------------------------------------
  subroutine output(Vx,Vy,P,istep)
!-----------------------------------------------------------------------------
! ■ 出力
!-----------------------------------------------------------------------------
  real(kind=8) :: Vx(NXmin:NXmax,NYmin:NYmax)
  real(kind=8) :: Vy(NXmin:NXmax,NYmin:NYmax)
  real(kind=8) :: P (NXmin:NXmax,NYmin:NYmax)
  real(kind=8) C1
  character(6) :: cistep
  write(cistep,'(i6.6)') istep
  C1=1.d0/(2.d0*dX)
  open(20,file='./data/velocity.'//cistep)
! open(21,file='./data/pressure.'//cistep)
! open(22,file='./data/vorticity.'//cistep)
  do iX=NXmin,NXmax,iSep
  do iY=NYmin,NYmax,iSep
     write(20,'(4e14.6)') dX*dble(iX),dX*dble(iY),Vx(iX,iY),Vy(iX,iY)
!    write(21,'(3e14.6)') dX*dble(iX),dX*dble(iY),P(iX,iY)
!    write(22,'(3e14.6)') dX*dble(iX),dX*dble(iY), &
!    C1*((Vx(iX,iY+1)-Vx(iX,iY-1))-(Vy(iX+1,iY)-Vy(iX-1,iY)))
  enddo
! write(21,*)
! write(22,*)
  enddo
  end subroutine output
!-----------------------------------------------------------------------------
  subroutine initial_condition(Vx,Vy,P)
!-----------------------------------------------------------------------------
! ■ 初期条件 ! y成分に小さい乱数を入れる
!-----------------------------------------------------------------------------
  real(kind=8) :: Vx(NXmin:NXmax,NYmin:NYmax)
  real(kind=8) :: Vy(NXmin:NXmax,NYmin:NYmax)
  real(kind=8) :: P (NXmin:NXmax,NYmin:NYmax)
  real(kind=8) X,Y
  call random_number(Vy)
  Vy(:,:)=2.d0*Vy(:,:)-1.d0 ! [-1:1] の乱数
  Vy(:,:)=Vy(:,:)*0.001d0
  do iX=NXmin,NXmax
  do iY=NYmin,NYmax
     X=dX*real(iX,8)
     Y=dX*real(iY,8)
     R=sqrt(X**2+Y**2)
     if (R.gt.D/2.d0) then
        Vx(iX,iY)=U
     else
        Vx(iX,iY)=0.d0
     endif
  enddo
  enddo
  Vy(NXmin,:)=0.d0
  Vy(:,NYmax)=0.d0
  Vy(:,NYmin)=0.d0
  call poisson(Vx,Vy,P)
  end subroutine initial_condition
!-----------------------------------------------------------------------------
  subroutine set_grid
!-----------------------------------------------------------------------------
! ■ 格子の設定
! iY1(iX) <---> iY2(iX) が円柱内 ( iX = [iXb1,iXb2] )
!-----------------------------------------------------------------------------
  real(kind=8) :: X,Y
  real(kind=8) :: twopi
  integer :: iX,iY
  dX=Xmax/dble(NXmax)
  Xmin=dble(NXmin)*dX
  Ymin=dble(NYmin)*dX
  Ymax=dble(NYmax)*dX
  iXb1=NXmax
  iXb2=NXmin
  do iX=NXmin,NXmax
  ichk=0
  do iY=NYmin,NYmax-1
     X=dX*dble(iX)
     Y=dX*dble(iY)
     if ((X**2+Y**2-(D/2.d0)**2)*(X**2+(Y+dX)**2-(D/2.d0)**2).lt.0.d0) then
        if (ichk.eq.0) then
           iY1(iX)=iY+1
           ichk=1
        else
           iY2(iX)=iY
        endif
     endif
  enddo
  if (ichk.eq.1) then
     iXb1=min(iXb1,iX)
     iXb2=max(iXb1,iX)
  endif
  enddo
  open(20,file='./data/grid.dat') 
  do iX=iXb1,iXb2
  do iY=iY1(iX),iY2(iX)
     X=dX*dble(iX)
     Y=dX*dble(iY)
     write(20,'(2e14.6)') X,Y
  enddo
  enddo
  close(20)
  open(20,file='./data/circle.dat') 
  twopi=8.d0*atan(1.d0)
  do i=0,200
     write(20,'(2e14.6)') (D/2.d0)*cos(real(i,8)*twopi/200), &
                          (D/2.d0)*sin(real(i,8)*twopi/200)
  end do
  close(20)
  end subroutine set_grid
end module cylinder
!-----------------------------------------------------------------------------
program main
  use cylinder
  implicit none
  real(kind=8) :: Vx(NXmin:NXmax,NYmin:NYmax)
  real(kind=8) :: Vy(NXmin:NXmax,NYmin:NYmax)
  real(kind=8) :: P (NXmin:NXmax,NYmin:NYmax)
  call set_grid
  call initial_condition(Vx,Vy,P)
  call output(Vx,Vy,P,0)
  open(30,file='time_series.dat')
  do istep=1,Nstep
     if (mod(istep,1000).eq.0) write(*,100) 'istep = ',istep, ', Vx(NXmax/2,0)=',Vx(NXmax/2,0)
     if (mod(istep,iout).eq.0) call output(Vx,Vy,P,istep)
     call march(Vx,Vy,P)
     write(30,'(3e14.6)') dt*real(istep),Vx(NXmax/2,0),Vy(NXmax/2,0)
  enddo
  close(30)
100 format(a,i6,a,f15.10)
end program main
!-----------------------------------------------------------------------------
