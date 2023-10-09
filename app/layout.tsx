import './globals.css'
import type { Metadata } from 'next'
import { Inter } from 'next/font/google'

const inter = Inter({ subsets: ['latin'] })

export const metadata: Metadata = {
  title: 'Island Generator',
  description: 'A shattered continent. A chain of fantastical islands.',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en" className='bg-slate-500 scrollbar'>
      <body className={`${inter.className}`}>{children}</body>
    </html>
  )
}
