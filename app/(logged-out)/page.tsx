import { Button } from '@/components/ui/button'
import React from 'react'
import {PersonStandingIcon} from 'lucide-react'
import Link from 'next/link'
import LightDarkToggle from '@/components/ui/light-dark-toggle'

const LandingPage = () => {
  return (
    <>
      <h1 className='flex gap-3 items-center'><PersonStandingIcon size={40} className='text-pink-500' />Fuck off</h1>
      <p>The best dashboard for customer support</p>
      
      <div className='flex gap-2 items-center'>
          <Button asChild>
            <Link href={'/login'}>Log in</Link>
          </Button>
          <small>or</small>
          <Button asChild variant={"outline"}>
            <Link href={'/sign-up'}>Sign up</Link>
          </Button>
          <LightDarkToggle />
      </div>
    </>
  )
}

export default LandingPage
 