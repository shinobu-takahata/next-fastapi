'use client'
import AppBar from '@mui/material/AppBar';
import Toolbar from '@mui/material/Toolbar';
import IconButton from '@mui/material/IconButton';
import Typography from '@mui/material/Typography';
import ResponsiveDrawer from './sidebar'; // 適切なパスに変更してください
import { useState } from 'react';

export default function MyAppBar() {
  const [mobileOpen, setMobileOpen] = useState(false);

  const handleDrawerToggle = () => {
    setMobileOpen(!mobileOpen);
  };

  return (
    <>
      <AppBar position="fixed" color='inherit' sx={{ display: { sm: 'none' } }}>
        <Toolbar>
          <IconButton
            color="inherit"
            aria-label="open drawer"
            edge="start"
            onClick={handleDrawerToggle}
            sx={{ mr: 2 }}
          >
            a
          </IconButton>
          <Typography variant="h6" noWrap component="div">
            Responsive Drawer
          </Typography>
        </Toolbar>
      </AppBar>
      <ResponsiveDrawer mobileOpen={mobileOpen} setMobileOpen={setMobileOpen} />
    </>
  );
}
