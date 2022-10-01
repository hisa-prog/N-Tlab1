import type { NextPage } from 'next'
import Head from 'next/head'
import Image from 'next/image'
import styles from '../styles/Home.module.css'

const Home: NextPage = () => {
  return (
    <div className='flex items-center justify-center mt-[20%]'>
      <div className='text-4xl flex flex-col w-max p-4 border-2 border-black rounded-lg'>
        <p className='text-center'>authorization</p>
        <div className='flex items-center mt-2'>
          <p>login</p>
          <input className='ml-2' />
        </div>
        <div className='flex items-center mt-2'>
          <p>password</p>
          <input className='ml-2' />
        </div>
      </div>
    </div>
  )
}

export default Home
