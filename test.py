import graphics.three_dimensional_graphics.camera
import graphics.three_dimensional_graphics.model
import locals
import pygame

cam = graphics.three_dimensional_graphics.camera.Camera(Width=1920, Height=1080, fov=90,
                                                        display_driver=locals.drivers.pygame.PYGAME_DRIVER,
                                                        special_flags=0)
                                                        #hdri="temporary res/hdr.hdr")


grid = graphics.three_dimensional_graphics.model.grid_mesh(0,0,0,25,25,1,5,cam)




pygame.init()

# cam.effect("breathing")
while 1:
    rx, ry = pygame.mouse.get_rel()

    cam.update_event_loop(exit_program_key=pygame.K_ESCAPE, camera_move_active_key=pygame.K_q)
    cam.rotation_input(rx * 1, ry * 1)
    cam.update()

    grid.project_render()

    pygame.display.flip()
