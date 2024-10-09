import React from 'react'


const LoggedOutLayout = ({children} : {children?: React.ReactNode}) => {
  return (
    <div className='flex flex-col min-h-screen items-center justify-center p-24 gap-4'>
       {children}
    </div>
  )
}

export default LoggedOutLayout
